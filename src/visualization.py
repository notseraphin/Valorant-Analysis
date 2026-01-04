import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os

sns.set_style("whitegrid")

FIG_DIR = "figures"
os.makedirs(FIG_DIR, exist_ok=True)

def save(fig_name):
    plt.tight_layout()
    plt.savefig(os.path.join(FIG_DIR, fig_name), dpi=300)
    plt.close()

# Scatter / Regression Plots

def plot_kd_vs_engagement(df):
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x="total_engagements", y="kd_ratio", alpha=0.6)
    sns.regplot(data=df, x="total_engagements", y="kd_ratio", scatter=False, color="red")
    plt.xlabel("Total Engagements (Kills + Deaths + Assists)")
    plt.ylabel("KD Ratio")
    plt.title("KD Ratio vs Total Engagements")
    save("kd_vs_engagement.png")


def plot_hs_vs_engagement(df):
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x="total_engagements", y="hs_percent", alpha=0.6)
    sns.regplot(data=df, x="total_engagements", y="hs_percent", scatter=False, color="red")
    plt.xlabel("Total Engagements")
    plt.ylabel("Headshot %")
    plt.title("Headshot % vs Total Engagements")
    save("hs_vs_engagement.png")

def plot_kd_vs_hs(df):
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x="kd_ratio", y="hs_percent", alpha=0.6)
    sns.regplot(data=df, x="kd_ratio", y="hs_percent", scatter=False, color="red")
    plt.xlabel("KD Ratio")
    plt.ylabel("Headshot %")
    plt.title("KD Ratio vs Headshot %")
    save("kd_vs_hs.png")

# Correlation Heatmap

def plot_correlation_heatmap(df):
    numeric_cols = ["kills", "deaths", "assists", "kd_ratio", "hs_percent", "score", "total_engagements", "win"]
    corr = df[numeric_cols].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
    plt.title("Correlation Heatmap")
    save("correlation_heatmap.png")

#  Win Distribution

def plot_win_distribution(df):
    plt.figure(figsize=(6, 4))
    sns.countplot(x="win", data=df, palette="viridis")
    plt.xlabel("Win (1) / Loss (0)")
    plt.ylabel("Number of Matches")
    plt.title("Win/Loss Distribution")
    save("win_distribution.png")

def plot_win_vs_kd(df):
    plt.figure(figsize=(8, 5))
    sns.boxplot(x="win", y="kd_ratio", data=df, palette="pastel")
    plt.xlabel("Win (1) / Loss (0)")
    plt.ylabel("KD Ratio")
    plt.title("KD Ratio Distribution by Match Outcome")
    save("win_vs_kd.png")

def plot_win_vs_hs(df):
    plt.figure(figsize=(8, 5))
    sns.boxplot(x="win", y="hs_percent", data=df, palette="pastel")
    plt.xlabel("Win (1) / Loss (0)")
    plt.ylabel("Headshot %")
    plt.title("Headshot % Distribution by Match Outcome")
    save("win_vs_hs.png")

# Agent / Map Analysis 

def plot_agent_winrate(df):
    agent_stats = df.groupby("agent")["win"].mean().sort_values(ascending=False)
    plt.figure(figsize=(10, 5))
    sns.barplot(x=agent_stats.index, y=agent_stats.values, palette="cool")
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Win Rate")
    plt.xlabel("Agent")
    plt.title("Win Rate by Agent")
    save("winrate_vs_agent.png")

def plot_map_winrate(df):
    map_stats = df.groupby("map")["win"].mean().sort_values(ascending=False)
    plt.figure(figsize=(8, 4))
    sns.barplot(x=map_stats.index, y=map_stats.values, palette="magma")
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Win Rate")
    plt.xlabel("Map")
    plt.title("Win Rate by Map")
    save("map_vs_winrate.png")

#  Engagement Analysis

def plot_engagement_histogram(df):
    plt.figure(figsize=(8, 5))
    sns.histplot(df["total_engagements"], bins=30, kde=True, color="skyblue")
    plt.xlabel("Total Engagements")
    plt.ylabel("Frequency")
    plt.title("Histogram of Total Engagements")
    save("engagement_histogram.png")

def plot_kd_histogram(df):
    plt.figure(figsize=(8, 5))
    sns.histplot(df["kd_ratio"], bins=30, kde=True, color="salmon")
    plt.xlabel("KD Ratio")
    plt.ylabel("Frequency")
    plt.title("Histogram of KD Ratios")
    save("kd_histogram.png")

def run_all(df): 
    plot_kd_vs_engagement(df)
    plot_hs_vs_engagement(df)
    plot_kd_vs_hs(df)
    plot_correlation_heatmap(df)
    plot_win_distribution(df)
    plot_win_vs_kd(df)
    plot_win_vs_hs(df)
    plot_agent_winrate(df)
    plot_map_winrate(df)
    plot_engagement_histogram(df)
    plot_kd_histogram(df)
    
