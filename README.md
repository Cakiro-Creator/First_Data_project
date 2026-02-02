# NHL Data Projekt

Dieses Projekt sammelt NHL-Teamstatistiken, bereinigt die Daten, prueft einfache
Qualitaetskriterien, erzeugt Features und erstellt eine kleine Visualisierung.

## Was passiert in der Pipeline
- Scrapy lädt die Rohdaten nach `data/raw/nhl.csv`
- Cleaning + Feature Engineering in `src/`
- Ergebnis als `data/processed/nhl_cleaned.csv`
- Plot als `reports/figures/top_teams.png`

## Schnellstart
```bash
pip install -r requirements.txt
python run_all.py
```

## Manuell ausfuehren
```bash
cd NHLScraper
scrapy crawl nhlscraper
cd ..
python src/run_pipeline.py
```

## Erwartete Ausgabe
- `data/processed/nhl_cleaned.csv`
- `reports/figures/top_teams.png`

## Projektstruktur
- `NHLScraper/`  Scrapy-Projekt (unveraendert)
- `data/`        Rohdaten und abgeleitete Daten
- `src/`         Cleaning, Checks, Features, Viz
- `notebooks/`   EDA/Spielwiese
- `reports/`     gespeicherte Plots

## Hinweise
- Rohdaten liegen in `data/raw/` (per `.gitignore` ausgeschlossen).
- Abgeleitete Daten sind reproduzierbar und koennen neu erstellt werden.

## Lizenz
Siehe `LICENSE`.
