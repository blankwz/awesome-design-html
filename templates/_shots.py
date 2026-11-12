"""Screenshot front.html + admin.html for every style template."""
import shutil
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(r"G:\AICODE\202610_design\awesome-design-md-main")
TPL = ROOT / "templates"
OUT = TPL / "_previews"
OUT.mkdir(exist_ok=True)
URL = "http://localhost:8765/templates/{style}/{page}.html"

styles = sorted(p.name for p in TPL.iterdir() if p.is_dir() and not p.name.startswith("_"))
print(f"{len(styles)} styles")

with sync_playwright() as pw:
    browser = pw.chromium.launch()
    page = browser.new_page(viewport={"width": 1360, "height": 900}, device_scale_factor=1)
    for i, s in enumerate(styles, 1):
        for page_name in ("front", "admin"):
            dest = TPL / s / f"{page_name}.png"
            try:
                page.goto(URL.format(style=s, page=page_name), wait_until="networkidle", timeout=30000)
            except Exception as e:
                print(f"[{i:02d}] {s}/{page_name}: networkidle timeout ({e.__class__.__name__}), continuing")
            page.wait_for_timeout(500)
            page.screenshot(path=str(dest), full_page=True)
            shutil.copy2(dest, OUT / f"{s}-{page_name}.png")
        print(f"[{i:02d}] {s} ok (front+admin)")
    browser.close()
print("done")
