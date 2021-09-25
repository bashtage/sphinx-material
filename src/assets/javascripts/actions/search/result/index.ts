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

import { translation } from "~/_"
import { round } from "~/utilities"

/* ----------------------------------------------------------------------------
 * Functions
 * ------------------------------------------------------------------------- */

/**
 * Set number of search results
 *
 * @param el - Search result metadata element
 * @param value - Number of results
 */
export function setSearchResultMeta(
  el: HTMLElement, value: number
): void {
  switch (value) {

    /* No results */
    case 0:
      el.textContent = translation("search.result.none")
      break

    /* One result */
    case 1:
      el.textContent = translation("search.result.one")
      break

    /* Multiple result */
    default:
      el.textContent = translation("search.result.other", round(value))
  }
}

/**
 * Reset number of search results
 *
 * @param el - Search result metadata element
 */
export function resetSearchResultMeta(
  el: HTMLElement
): void {
  el.textContent = translation("search.result.placeholder")
}

/* ------------------------------------------------------------------------- */

/**
 * Add an element to the search result list
 *
 * @param el - Search result list element
 * @param child - Search result element
 */
export function addToSearchResultList(
  el: HTMLElement, child: Element
): void {
  el.appendChild(child)
}

/**
 * Reset search result list
 *
 * @param el - Search result list element
 */
export function resetSearchResultList(
  el: HTMLElement
): void {
  el.innerHTML = ""
}
