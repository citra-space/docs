#!/usr/bin/env python3
"""Capture a screenshot of a specific UI element using Playwright.

Usage:
    python scripts/screenshots/capture.py \
        --url "http://localhost:24872/#monitoring" \
        --selector "#globalStatusBar" \
        --output "docs/citrascope/img/status-bar.png" \
        --wait-for "#globalStatusBar" \
        --click "a:has-text('Hardware')" \
        --hide "#logAccordion" \
        --viewport 1280x800
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright


def main():
    parser = argparse.ArgumentParser(description="Screenshot a UI element with Playwright")
    parser.add_argument("--url", required=True, help="URL to navigate to")
    parser.add_argument("--selector", required=True, help="CSS selector of the element to capture")
    parser.add_argument("--output", required=True, help="Output PNG file path")
    parser.add_argument("--wait-for", dest="wait_for", help="Wait for this selector to be visible before acting")
    parser.add_argument("--click", action="append", default=[], help="Click this selector before capture (repeatable)")
    parser.add_argument(
        "--hide", action="append", default=[], help="Hide elements matching this CSS selector before capture (repeatable)"
    )
    parser.add_argument("--viewport", default="1280x800", help="Viewport size as WIDTHxHEIGHT (default: 1280x800)")
    parser.add_argument("--timeout", type=int, default=10000, help="Timeout in ms for waits/actions (default: 10000)")
    args = parser.parse_args()

    width, height = (int(d) for d in args.viewport.split("x"))
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": width, "height": height})

        page.goto(args.url, wait_until="networkidle")

        if args.wait_for:
            page.locator(args.wait_for).wait_for(state="visible", timeout=args.timeout)

        for click_sel in args.click:
            page.locator(click_sel).click(timeout=args.timeout)
            page.wait_for_timeout(300)

        for hide_sel in args.hide:
            page.evaluate(
                """sel => document.querySelectorAll(sel).forEach(el => el.style.display = 'none')""",
                hide_sel,
            )

        element = page.locator(args.selector)
        element.wait_for(state="visible", timeout=args.timeout)
        element.screenshot(path=str(output_path))

        browser.close()

    print(f"Saved: {output_path}")


if __name__ == "__main__":
    main()
