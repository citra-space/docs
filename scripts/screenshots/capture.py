#!/usr/bin/env python3
"""Capture a screenshot of a specific UI element using Playwright.

Usage:
    python scripts/screenshots/capture.py \
        --url "http://localhost:24872/#monitoring" \
        --selector "#globalStatusBar" \
        --output "docs/citrasense/img/status-bar.png" \
        --wait-for "#globalStatusBar" \
        --click "a:has-text('Hardware')" \
        --hide "#logAccordion" \
        --viewport 1280x800

Annotated highlights:
    Add a red outline on specific elements before capturing. Padding (--pad)
    widens the clip box so the outline/shadow aren't cropped off. If --pad
    isn't given but --highlight is, a safe default of 24px is used.

    python scripts/screenshots/capture.py \
        --url "http://localhost:24872/#monitoring" \
        --selector ".card:has(.card-header:has-text('Telescope'))" \
        --highlight "button:has-text('Align Now')" \
        --output "docs/citrasense/img/operating-align-now.png"
"""

from __future__ import annotations

import argparse
from pathlib import Path

from playwright.sync_api import sync_playwright

HIGHLIGHT_CLASS = "__doc_highlight__"
HIGHLIGHT_CSS = f"""
.{HIGHLIGHT_CLASS} {{
    outline: 3px solid #ff3b30 !important;
    outline-offset: 3px !important;
    border-radius: 4px !important;
    box-shadow: 0 0 14px rgba(255, 59, 48, 0.75) !important;
    position: relative !important;
    z-index: 100 !important;
}}
"""
# Covers 3px outline + 3px offset + 14px box-shadow blur with slack.
DEFAULT_HIGHLIGHT_PAD = 24


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
    parser.add_argument(
        "--highlight",
        action="append",
        default=[],
        help=(
            "Add a red outline highlight to elements matching this selector before capture "
            "(repeatable). Applies to every match of the selector. Implies --pad if --pad is 0."
        ),
    )
    parser.add_argument(
        "--pad",
        type=int,
        default=0,
        help=(
            "Padding in px around the captured element. Useful to keep highlight outlines or "
            f"shadows in frame. Default: 0, or {DEFAULT_HIGHLIGHT_PAD} when --highlight is used."
        ),
    )
    parser.add_argument("--viewport", default="1280x800", help="Viewport size as WIDTHxHEIGHT (default: 1280x800)")
    parser.add_argument("--timeout", type=int, default=10000, help="Timeout in ms for waits/actions (default: 10000)")
    args = parser.parse_args()

    width, height = (int(d) for d in args.viewport.split("x"))
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    pad = args.pad if args.pad > 0 else (DEFAULT_HIGHLIGHT_PAD if args.highlight else 0)

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

        if args.highlight:
            page.add_style_tag(content=HIGHLIGHT_CSS)
            for hl_sel in args.highlight:
                # evaluate_all covers every match — scope the selector tighter if you
                # only want one. :has-text() works because this is a Playwright locator.
                page.locator(hl_sel).evaluate_all(
                    f"els => els.forEach(el => el.classList.add('{HIGHLIGHT_CLASS}'))"
                )

        element = page.locator(args.selector)
        element.wait_for(state="visible", timeout=args.timeout)
        element.scroll_into_view_if_needed()
        page.wait_for_timeout(150)

        if pad > 0:
            box = element.bounding_box()
            if box is None:
                raise RuntimeError(f"bounding_box() returned None for selector: {args.selector}")
            viewport = page.viewport_size or {"width": width, "height": height}
            x = max(0, box["x"] - pad)
            y = max(0, box["y"] - pad)
            right = min(viewport["width"], box["x"] + box["width"] + pad)
            bottom = min(viewport["height"], box["y"] + box["height"] + pad)
            page.screenshot(
                path=str(output_path),
                clip={"x": x, "y": y, "width": right - x, "height": bottom - y},
            )
        else:
            element.screenshot(path=str(output_path))

        browser.close()

    print(f"Saved: {output_path}")


if __name__ == "__main__":
    main()
