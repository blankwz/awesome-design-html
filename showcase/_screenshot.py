"""Screenshot every style showcase to its folder + a shared _previews folder."""
import shutil
from pathlib import Path

from playwright.sync_api import sync_playwright

BASE = Path(r"G:\AICODE\202610_design\awesome-design-md-main\showcase")
OUT = BASE / "_previews"
OUT.mkdir(exist_ok=True)
URL = "http://localhost:8765/showcase/{style}/index.html"

styles = sorted(p.name for p in BASE.iterdir() if p.is_dir() and not p.name.startswith("_"))
print(f"{len(styles)} styles")

with sync_playwright() as pw:
    browser = pw.chromium.launch()
    page = browser.new_page(viewport={"width": 1280, "height": 900}, device_scale_factor=1)
    for i, s in enumerate(styles, 1):
        dest = BASE / s / "preview.png"
        try:
            page.goto(URL.format(style=s), wait_until="networkidle", timeout=30000)
        except Exception as e:
            print(f"[{i:02d}] {s}: networkidle timeout ({e.__class__.__name__}), continuing")
        page.wait_for_timeout(600)  # let webfonts settle
        page.screenshot(path=str(dest), full_page=True)
        shutil.copy2(dest, OUT / f"{s}.png")
        print(f"[{i:02d}] {s} ok")
    browser.close()
print("done")
