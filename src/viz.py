# viz.py
# Einfache Visualisierung
import matplotlib.pyplot as plt
def plot_top_teams(df, out_path=None):
    top = (
        df.groupby("Team_Initials")["Wins"]
          .mean()
          .sort_values(ascending=False)
          .head(10)
          .sort_values()
    )
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(top.index, top.values)
    ax.set_title("Top Teams by Average Wins")
    ax.set_xlabel("Average Wins")
    ax.set_ylabel("Teams")
    ax.grid(axis="x", linestyle="--", alpha=0.5)
    plt.tight_layout()
    if out_path:
        fig.savefig(out_path, dpi=150)
    else:
        plt.show()
