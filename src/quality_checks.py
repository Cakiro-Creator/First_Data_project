# quality_checks.py
# Einfache Plausibilitaetschecks
def validate(df):
    checks = {
        "no_missing_team": df["Team_Name"].notna().all(),
        "year_range_ok": df["Year"].between(1990, 2011).all(),
        "wins_non_negative": (df["Wins"] >= 0).all(),
        "losses_non_negative": (df["Losses"] >= 0).all(),
        "goal_diff_consistent": (df["Goal_Differential"] == (df["Goals_For"] - df["Goals_Against"])).all(),
    }
    return checks
