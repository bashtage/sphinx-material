/*
 * Copyright (c) 2016-2021 Martin Donath <martin.donath@squidfunk.com>
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to
 * deal in the Software without restriction, including without limitation the
 * rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
 * sell copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
 * IN THE SOFTWARE.
 */

import {
  EMPTY,
  NEVER,
  Observable,
  Subject,
  fromEvent,
  merge,
  of
} from "rxjs"
import {
  bufferCount,
  catchError,
  concatMap,
  debounceTime,
  distinctUntilChanged,
  distinctUntilKeyChanged,
  filter,
  map,
  sample,
  share,
  skip,
  skipUntil,
  switchMap
} from "rxjs/operators"

import { configuration } from "~/_"
import {
  Viewport,
  ViewportOffset,
  createElement,
  getElement,
  getElements,
  replaceElement,
  request,
  requestXML,
  setLocation,
  setLocationHash,
  setViewportOffset
} from "~/browser"
import { getComponentElement } from "~/components"

/* ----------------------------------------------------------------------------
 * Types
 * ------------------------------------------------------------------------- */

/**
 * History state
 */
export interface HistoryState {
  url: URL                             /* State URL */
  offset?: ViewportOffset              /* State viewport offset */
}

/* ----------------------------------------------------------------------------
 * Helper types
 * ------------------------------------------------------------------------- */

/**
 * Setup options
 */
interface SetupOptions {
  document$: Subject<Document>         /* Document subject */
  location$: Subject<URL>              /* Location subject */
  viewport$: Observable<Viewport>      /* Viewport observable */
}

/* ----------------------------------------------------------------------------
 * Helper functions
 * ------------------------------------------------------------------------- */

/**
 * Preprocess a list of URLs
 *
 * This function replaces the `site_url` in the sitemap with the actual base
 * URL, to allow instant loading to work in occasions like Netlify previews.
 *
 * @param urls - URLs
 *
 * @returns Processed URLs
 */
function preprocess(urls: string[]): string[] {
  if (urls.length < 2)
    return urls

  /* Take the first two URLs and remove everything after the last slash */
  const [root, next] = urls
    .sort((a, b) => a.length - b.length)
    .map(url => url.replace(/[^/]+$/, ""))

  /* Compute common prefix */
  let index = 0
  if (root === next)
    index = root.length
  else
    while (root.charCodeAt(index) === next.charCodeAt(index))
      index++

  /* Replace common prefix (i.e. base) with effective base */
  const config = configuration()
  return urls.map(url => (
    url.replace(root.slice(0, index), `${config.base}/`)
  ))
}

/* ----------------------------------------------------------------------------
 * Functions
 * ------------------------------------------------------------------------- */

/**
 * Set up instant loading
 *
 * When fetching, theoretically, we could use `responseType: "document"`, but
 * since all MkDocs links are relative, we need to make sure that the current
 * location matches the document we just loaded. Otherwise any relative links
 * in the document could use the old location.
 *
 * This is the reason why we need to synchronize history events and the process
 * of fetching the document for navigation changes (except `popstate` events):
 *
 * 1. Fetch document via `XMLHTTPRequest`
 * 2. Set new location via `history.pushState`
 * 3. Parse and emit fetched document
 *
 * For `popstate` events, we must not use `history.pushState`, or the forward
 * history will be irreversibly overwritten. In case the request fails, the
 * location change is dispatched regularly.
 *
 * @param options - Options
 */
export function setupInstantLoading(
  { document$, location$, viewport$ }: SetupOptions
): void {
  const config = configuration()
  if (location.protocol === "file:")
    return

  /* Disable automatic scroll restoration */
  if ("scrollRestoration" in history) {
    history.scrollRestoration = "manual"

    /* Hack: ensure that reloads restore viewport offset */
    fromEvent(window, "beforeunload")
      .subscribe(() => {
        history.scrollRestoration = "auto"
      })
  }

  /* Hack: ensure absolute favicon link to omit 404s when switching */
  const favicon = getElement<HTMLLinkElement>("link[rel=icon]")
  if (typeof favicon !== "undefined")
    favicon.href = favicon.href

  /* Intercept internal navigation */
  const push$ = requestXML(`${config.base}/sitemap.xml`)
    .pipe(
      map(sitemap => preprocess(getElements("loc", sitemap)
        .map(node => node.textContent!)
      )),
      switchMap(urls => fromEvent<MouseEvent>(document.body, "click")
        .pipe(
          filter(ev => !ev.metaKey && !ev.ctrlKey),
          switchMap(ev => {

            /* Handle HTML and SVG elements */
            if (ev.target instanceof Element) {
              const el = ev.target.closest("a")
              if (el && !el.target && urls.includes(el.href)) {
                ev.preventDefault()
                return of({
                  url: new URL(el.href)
                })
              }
            }
            return NEVER
          })
        )
      ),
      share<HistoryState>()
    )

  /* Intercept history back and forward */
  const pop$ = fromEvent<PopStateEvent>(window, "popstate")
    .pipe(
      filter(ev => ev.state !== null),
      map(ev => ({
        url: new URL(location.href),
        offset: ev.state
      })),
      share<HistoryState>()
    )

  /* Emit location change */
  merge(push$, pop$)
    .pipe(
      distinctUntilChanged((a, b) => a.url.href === b.url.href),
      map(({ url }) => url)
    )
      .subscribe(location$)

  /* Fetch document via `XMLHTTPRequest` */
  const response$ = location$
    .pipe(
      distinctUntilKeyChanged("pathname"),
      switchMap(url => request(url.href)
        .pipe(
          catchError(() => {
            setLocation(url)
            return NEVER
          })
        )
      ),
      share()
    )

  /* Set new location via `history.pushState` */
  push$
    .pipe(
      sample(response$)
    )
      .subscribe(({ url }) => {
        history.pushState({}, "", `${url}`)
      })

  /* Parse and emit fetched document */
  const dom = new DOMParser()
  response$
    .pipe(
      switchMap(res => res.text()),
      map(res => dom.parseFromString(res, "text/html"))
    )
      .subscribe(document$)

  /* Emit history state change */
  merge(push$, pop$)
    .pipe(
      sample(document$)
    )
      .subscribe(({ url, offset }) => {
        if (url.hash && !offset)
          setLocationHash(url.hash)
        else
          setViewportOffset(offset || { y: 0 })
      })

  const loadedScriptUrls = new Set<string>()
  const loadedInlineScripts = new Set<string>()
  for (const el of getElements("script", document)) {
    if (el.src) {
      loadedScriptUrls.add(new URL(el.src, document.baseURI).toString())
    } else {
      loadedInlineScripts.add(el.outerHTML)
    }
  }

  /* Replace meta tags and components */
  document$
    .pipe(
      skip(1),
      concatMap(async replacement => {
        for (const selector of [

          /* Meta tags */
          "title",
          "link[rel=canonical]",
          "meta[name=author]",
          "meta[name=description]",

          /* Components */
          "[data-md-component=announce]",
          "[data-md-component=container]",
          "[data-md-component=header-topic]",
          "[data-md-component=logo], .md-logo", // compat
          "[data-md-component=skip]"
        ]) {
          const source = getElement(selector)
          const target = getElement(selector, replacement)
          if (
            typeof source !== "undefined" &&
            typeof target !== "undefined"
          ) {
            replaceElement(source, target)
          }
        }

        /* Run-run MathJax if already loaded */
        // eslint-disable-next-line @typescript-eslint/no-explicit-any
        if ((window as any).MathJax?.typesetPromise !== undefined) {
          // eslint-disable-next-line @typescript-eslint/no-explicit-any
          await (window as any).MathJax.typesetPromise()
        }

        /* Insert scripts */
        for (const el of getElements("script", replacement)) {
          if (el.src) {
            const url = new URL(el.src, document.baseURI).toString()
            if (!loadedScriptUrls.has(url)) {
              const script = createElement("script")
              for (const name of el.getAttributeNames()) {
                script.setAttribute(name, el.getAttribute(name)!)
              }
              let promise: Promise<void>|undefined
              script.src = url
              if (!script.async) {
                promise = new Promise(resolve => script.addEventListener("load", () => resolve()))
              }
              document.body.appendChild(script)
              loadedScriptUrls.add(url)
              if (promise !== undefined) await promise
            }
          } else {
            const outerHTML = el.outerHTML
            if (!loadedInlineScripts.has(outerHTML)) {
              const script = createElement("script")
              for (const name of el.getAttributeNames()) {
                script.setAttribute(name, el.getAttribute(name)!)
              }
              script.textContent = el.textContent
              document.body.appendChild(script)
              loadedInlineScripts.add(outerHTML)
            }
          }
        }
      })
    ).subscribe()

  /* Re-evaluate scripts */
  document$
    .pipe(
      skip(1),
      map(() => getComponentElement("container")),
      switchMap(el => of(...getElements("script", el))),
      concatMap(el => {
        const script = createElement("script")
        if (el.src) {
          for (const name of el.getAttributeNames())
            script.setAttribute(name, el.getAttribute(name)!)
          replaceElement(el, script)

          /* Complete when script is loaded */
          return new Observable(observer => {
            script.onload = () => observer.complete()
          })

        /* Complete immediately */
        } else {
          script.textContent = el.textContent
          replaceElement(el, script)
          return EMPTY
        }
      })
    )
      .subscribe()

  /* Debounce update of viewport offset */
  viewport$
    .pipe(
      skipUntil(push$),
      debounceTime(250),
      distinctUntilKeyChanged("offset")
    )
      .subscribe(({ offset }) => {
        history.replaceState(offset, "")
      })

  /* Set viewport offset from history */
  merge(push$, pop$)
    .pipe(
      bufferCount(2, 1),
      filter(([a, b]) => a.url.pathname === b.url.pathname),
      map(([, state]) => state)
    )
      .subscribe(({ offset }) => {
        setViewportOffset(offset || { y: 0 })
      })
}
