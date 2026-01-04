from pathlib import Path
import pandas as pd

def load_data(csv_file: Path) -> pd.DataFrame:
    df = pd.read_csv(csv_file)
    df["total_engagements"] = df["kills"] + df["deaths"] + df["assists"]
    return df
