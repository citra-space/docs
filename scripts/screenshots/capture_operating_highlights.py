"""Capture the annotated screenshot series used in the Operating CitraScope guide.

This is a *series* capture script — it opens the Monitoring tab once and takes
several small, focused screenshots, each with a red highlight on a specific
control. Series capture is worth the custom script when you want:

  * Multiple shots reusing the same page/state (faster, fewer cold loads)
  * Compound framing — highlight *inside* element A, crop to element B
  * Multiple highlights in one frame (e.g., two toggle switches together)

For one-off annotated shots, prefer the CLI:

    scripts/screenshots/capture.py --highlight SELECTOR ...

The CLI shares the same highlight CSS and padded-clip math; this file is the
canonical template to copy when you need a series.

## Mechanics

1. Inject highlight CSS once (`add_style_tag`).
2. For each shot: add the `__doc_highlight__` class to the target, wait for
   reflow, compute a padded clip box around the crop locator, capture with
   `page.screenshot(clip=...)`, then strip the class.
3. Padding (24px) keeps the 3px outline + 3px offset + 14px box-shadow blur
   from being cropped when the highlight sits flush against the crop edge.

Run with the docs venv:

    .venv/bin/python3 scripts/screenshots/capture_operating_highlights.py
"""

from __future__ import annotations

from pathlib import Path

from playwright.sync_api import Locator, Page, sync_playwright

# Resolve relative to the repo root (this file lives in scripts/screenshots/).
REPO_ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = REPO_ROOT / "docs" / "citrascope" / "img"
URL = "http://localhost:24872/#monitoring"
VIEWPORT = {"width": 1280, "height": 900}

# Pad around the crop locator so the red highlight (3px outline + 3px offset +
# 14px box-shadow blur) isn't clipped by the element's bounding box.
HIGHLIGHT_PAD = 24

HIGHLIGHT_CSS = """
.__doc_highlight__ {
    outline: 3px solid #ff3b30 !important;
    outline-offset: 3px !important;
    border-radius: 4px !important;
    box-shadow: 0 0 14px rgba(255, 59, 48, 0.75) !important;
    position: relative !important;
    z-index: 100 !important;
}
"""


def highlight(locator: Locator) -> None:
    """Add the highlight class to the element matched by this Playwright locator."""
    locator.first.evaluate("el => el.classList.add('__doc_highlight__')")


def clear_highlights(page: Page) -> None:
    page.evaluate(
        """() => {
            document.querySelectorAll('.__doc_highlight__').forEach(el => {
                el.classList.remove('__doc_highlight__');
            });
        }"""
    )


def shot(page: Page, locator: Locator, filename: str) -> None:
    """Capture `locator` with padded clipping so highlights stay in frame."""
    locator.wait_for(state="visible", timeout=10_000)
    locator.scroll_into_view_if_needed()
    # Allow reflow/repaint after highlight injection + scroll.
    page.wait_for_timeout(150)

    box = locator.bounding_box()
    if box is None:
        raise RuntimeError(f"Could not get bounding box for {filename}")

    viewport = page.viewport_size or VIEWPORT
    x = max(0, box["x"] - HIGHLIGHT_PAD)
    y = max(0, box["y"] - HIGHLIGHT_PAD)
    right = min(viewport["width"], box["x"] + box["width"] + HIGHLIGHT_PAD)
    bottom = min(viewport["height"], box["y"] + box["height"] + HIGHLIGHT_PAD)
    clip = {"x": x, "y": y, "width": right - x, "height": bottom - y}

    page.screenshot(path=str(OUT_DIR / filename), clip=clip)
    print(f"Saved {filename}")


def run() -> None:
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        page = browser.new_page(viewport=VIEWPORT)
        page.goto(URL, wait_until="networkidle")
        page.locator("#globalStatusBar").wait_for(state="visible", timeout=10_000)

        # Inject highlight CSS once.
        page.add_style_tag(content=HIGHLIGHT_CSS)

        # Hide the log accordion so it doesn't distort the layout when cards reflow.
        page.evaluate(
            "() => { const el = document.querySelector('#logAccordion'); if (el) el.style.display = 'none'; }"
        )

        telescope_card = page.locator('.card:has(.card-header:has-text("Telescope"))')
        optics_card = page.locator('.card:has(.card-header:has-text("Optics"))')

        pointing_model_box = telescope_card.locator(
            'div.mt-3.pt-3.border-top:has(> div > span.fw-semibold.small:has-text("Pointing Model"))'
        ).first
        mount_controls = telescope_card.locator(
            'div.mt-3.pt-3.border-top:has(button:has-text("Align Now"))'
        ).first
        autofocus_box = optics_card.locator(
            'div.pt-2.mt-2.border-top:has(button:has-text("Autofocus"))'
        ).first

        # ── 1. Reset button highlighted within the Pointing Model box ──
        highlight(pointing_model_box.locator('button.btn-outline-danger:has-text("Reset")'))
        shot(page, pointing_model_box, "operating-reset-highlight.png")
        clear_highlights(page)

        # ── 2. Calibrate button highlighted within the Pointing Model box ──
        highlight(pointing_model_box.locator('button:has-text("Calibrate")'))
        shot(page, pointing_model_box, "operating-calibrate-highlight.png")
        clear_highlights(page)

        # ── 3. Jog pad highlighted within the mount controls ──
        highlight(mount_controls.locator('div[style*="grid-template-columns: repeat(3, 36px)"]'))
        shot(page, mount_controls, "operating-jog-pad-highlight.png")
        clear_highlights(page)

        # ── 4. Align Now button highlighted within the mount controls ──
        highlight(mount_controls.locator('button:has-text("Align Now")'))
        shot(page, mount_controls, "operating-align-now-highlight.png")
        clear_highlights(page)

        # ── 5. Snap button highlighted — crop to the camera controls row ──
        camera_controls = optics_card.locator(
            'div.d-flex.align-items-end.gap-2.flex-wrap:has(button:has-text("Snap"))'
        ).first
        highlight(optics_card.locator('button:has-text("Snap")'))
        shot(page, camera_controls, "operating-snap-highlight.png")
        clear_highlights(page)

        # ── 6. Autofocus button highlighted within the autofocus subsection ──
        highlight(optics_card.locator('button:has-text("Autofocus")'))
        shot(page, autofocus_box, "operating-autofocus-highlight.png")
        clear_highlights(page)

        # ── 7. Request Batch button highlighted — crop to the Scheduled Tasks header ──
        scheduled_card = page.locator('.card:has(.card-header:has-text("Scheduled Tasks"))')
        scheduled_header = scheduled_card.locator("> .card-header").first
        highlight(scheduled_card.locator('button:has-text("Request Batch")'))
        shot(page, scheduled_header, "operating-request-batch-highlight.png")
        clear_highlights(page)

        # ── 8. Scheduling + Processing switches highlighted in status bar ──
        status_bar = page.locator("#globalStatusBar")
        switches_row = status_bar.locator("div.w-100.d-flex.flex-wrap").first
        highlight(
            status_bar.locator('div.d-flex.align-items-center.gap-1:has(small:has-text("Scheduling"))')
        )
        highlight(
            status_bar.locator('div.d-flex.align-items-center.gap-1:has(small:has-text("Processing"))')
        )
        shot(page, switches_row, "operating-switches-highlight.png")
        clear_highlights(page)

        browser.close()


if __name__ == "__main__":
    run()
