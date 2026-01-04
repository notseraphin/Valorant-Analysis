from pathlib import Path
from src.data_processing import load_data
from src.visualization import run_all
from src.modeling import logistic_analysis, kd_win_curve

CSV_FILE = Path("data") / "matches.csv"
FIGURE_PATH = Path("figures") / "kd_vs_engagement.png"

def main():
    df = load_data(CSV_FILE)
    run_all(df)

    results = logistic_analysis(df)
    print("Accuracy:", results["accuracy"])
    print("Feature Importance:\n", results["feature_importance"])

    curves = kd_win_curve(df)
    for p, kd in curves.items():
        print(f"KD needed for {int(p*100)}% win chance: {kd:.3f}")

if __name__ == "__main__":
    main()
