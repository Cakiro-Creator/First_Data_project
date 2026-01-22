# features.py
# Kleine Feature-Ideen fuer Analysen
import pandas as pd
import numpy as np
import re
def add_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["Games_played"] = df["Wins"] + df["Losses"] + df["Overtime_Losses"]
    df.loc[df["Games_played"] == 0, "Games_played"] = pd.NA
    df["GF_per_Game"] = (df["Goals_For"] / df["Games_played"]).round(2)
    df["GA_per_Game"] = (df["Goals_Against"] / df["Games_played"]).round(2)
    df["GD_per_Game"] = (df["Goal_Differential"] / df["Games_played"]).round(2)
    def initials(name: str) -> str:
        words = re.findall(r"[A-Za-z]+", str(name))
        return "".join(w[0].upper() for w in words if w)
    df["Team_Initials"] = df["Team_Name"].apply(initials)
    df["Era"] = np.where(df["Year"] < 2000, "1990s", "2000s")
    return df
