from pathlib import Path
import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("HENDRIK_API_KEY")
REGION = "na"
NAME = "Baguette"
TAG = "GRAlN"
CSV_FILE = Path("data") / "matches.csv"

HEADERS = {"Authorization": API_KEY}

def fetch_matches(region=REGION, name=NAME, tag=TAG):
    url = f"https://api.henrikdev.xyz/valorant/v1/stored-matches/{region}/{name}/{tag}"
    matches = []
    page = 1
    while True:
        params = {"page": page, "size": 100}
        resp = requests.get(url, headers=HEADERS, params=params)
        if resp.status_code != 200:
            print(f"API Error: {resp.status_code}, {resp.json()}")
            break
        data = resp.json().get("data", [])
        if not data:
            break
        matches.extend(data)
        if len(data) < params["size"]:
            break
        page += 1
    print(f"Fetched {len(matches)} matches")
    return matches

def process_match(match):
    meta = match.get("meta", {})
    stats = match.get("stats", {})
    teams = match.get("teams", {})
    team_name = stats.get("team")
    win = None
    if team_name and teams:
        player_team_score = teams.get(team_name.lower())
        other_team_score = sum(v for k, v in teams.items() if k.lower() != team_name.lower())
        if player_team_score is not None:
            win = int(player_team_score > other_team_score)
    shots = stats.get("shots", {})
    headshots = shots.get("head", 0)
    bodyshots = shots.get("body", 0)
    legshots = shots.get("leg", 0)
    total_shots = headshots + bodyshots + legshots
    hs_percent = (headshots / total_shots * 100) if total_shots > 0 else 0
    kills = stats.get("kills", 0)
    deaths = stats.get("deaths", 0)
    kd_ratio = kills / deaths if deaths not in (0, None) else kills
    return {
        "match_id": meta.get("id"),
        "map": meta.get("map", {}).get("name"),
        "game_start": meta.get("started_at"),
        "agent": stats.get("character", {}).get("name"),
        "kills": kills,
        "deaths": deaths,
        "assists": stats.get("assists"),
        "score": stats.get("score"),
        "shots_total": total_shots,
        "hs_percent": hs_percent,
        "kd_ratio": kd_ratio,
        "win": win
    }

def save_matches_csv(csv_path=CSV_FILE):
    raw = fetch_matches()
    if not raw:
        print("No matches fetched.")
        return
    df = pd.DataFrame([process_match(m) for m in raw])
    df.to_csv(csv_path, index=False)
    print(f"Saved {len(df)} matches to {csv_path}")

if __name__ == "__main__":
    save_matches_csv()
