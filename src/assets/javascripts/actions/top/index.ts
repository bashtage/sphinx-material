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

/* ----------------------------------------------------------------------------
 * Functions
 * ------------------------------------------------------------------------- */

/**
 * Set back-to-top state
 *
 * @param el - Back-to-top element
 * @param state - Back-to-top state
 */
export function setBackToTopState(
  el: HTMLElement, state: "hidden"
): void {
  el.setAttribute("data-md-state", state)
}

/**
 * Reset back-to-top state
 *
 * @param el - Back-to-top element
 */
export function resetBackToTopState(
  el: HTMLElement
): void {
  el.removeAttribute("data-md-state")
}

/* ------------------------------------------------------------------------- */

/**
 * Set back-to-top offset
 *
 * @param el - Back-to-top element
 * @param value - Back-to-top offset
 */
export function setBackToTopOffset(
  el: HTMLElement, value: number
): void {
  el.style.top = `${value}px`
}

/**
 * Reset back-to-top offset
 *
 * @param el - Back-to-top element
 */
export function resetBackToTopOffset(
  el: HTMLElement
): void {
  el.style.top = ""
}
