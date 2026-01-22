# run_pipeline.py
# Laeuft die einfache Pipeline von Rohdaten bis Plot
import pandas as pd
from pathlib import Path
from cleaning import clean
from quality_checks import validate
from features import add_features
from viz import plot_top_teams
def main():
    root = Path(__file__).resolve().parents[1]
    input_csv = root / "data" / "raw" / "nhl.csv"
    output_csv = root / "data" / "processed" / "nhl_cleaned.csv"
    output_plot = root / "reports" / "figures" / "top_teams.png"
    if not input_csv.exists():
        print(f"Missing input: {input_csv}")
        print("Run the scraper first: scrapy crawl nhlscraper")
        return
    df = pd.read_csv(input_csv)
    df = clean(df)
    df = add_features(df)
    checks = validate(df)
    print("Checks:")
    for k, v in checks.items():
        print(f"- {k}: {v}")
    output_csv.parent.mkdir(parents=True, exist_ok=True)
    output_plot.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_csv, index=False)
    plot_top_teams(df, out_path=output_plot)
    print(f"Saved: {output_csv}")
    print(f"Saved: {output_plot}")
if __name__ == "__main__":
    main()
