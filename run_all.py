# run_all.py
# Laeuft Scraper und danach die Pipeline
import subprocess
import sys
from pathlib import Path


def main():
    root = Path(__file__).resolve().parent
    scraper_dir = root / "NHLScraper"
    pipeline_script = root / "src" / "run_pipeline.py"
    (root / "data" / "raw").mkdir(parents=True, exist_ok=True)

    subprocess.run(
        [sys.executable, "-m", "scrapy", "crawl", "nhlscraper"],
        cwd=str(scraper_dir),
        check=True,
    )
    subprocess.run([sys.executable, str(pipeline_script)], check=True)


if __name__ == "__main__":
    main()
