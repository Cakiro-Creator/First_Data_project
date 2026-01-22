# cleaning.py
# Einfache Reinigung: Typen, Leerzeichen, fehlende Werte
import pandas as pd
def clean(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["Team_Name"] = df["Team_Name"].astype(str).str.strip()
    df["Year"] = pd.to_datetime(df["Year"], errors="coerce").dt.year
    num_cols = [
        "Wins",
        "Losses",
        "Overtime_Losses",
        "Goals_For",
        "Goals_Against",
        "Goal_Differential",
        "Win_Percentage",
    ]
    for col in num_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    if df["Win_Percentage"].max() <= 1:
        df["Win_Percentage"] = (df["Win_Percentage"] * 100).round(2)
    df["Overtime_Losses"] = df["Overtime_Losses"].fillna(0).astype(int)
    for col in num_cols:
        if df[col].isna().any():
            df[col] = df[col].fillna(df[col].median())
    return df
