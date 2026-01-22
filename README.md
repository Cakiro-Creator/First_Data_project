# NHL Data Projekt (simpel)

Kurz und knackig:
- NHLScraper bleibt wie er ist.
- Pipeline liest data/raw/nhl.csv.
- Output geht nach data/processed/nhl_cleaned.csv.
- Ein Plot landet in reports/figures/.

## Schnellstart
1) Alles in einem Schritt
   - `python run_all.py`
2) Oder manuell:
   - im Ordner `NHLScraper`: `scrapy crawl nhlscraper`
   - `python src/run_pipeline.py`

## Struktur
- `NHLScraper/`  Scrapy Projekt (unveraendert)
- `data/`        raw, processed, sample
- `src/`         Cleaning, Checks, Features, Viz
- `notebooks/`   einfache EDA
- `reports/`     gespeicherte Plots
