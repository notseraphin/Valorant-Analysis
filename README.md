# Valorant-Analysis

**Match-Level Player Statistics & Trend Analysis**

***Overview***

This project analyzes Valorant match performance data to study player trends, agent usage, and performance consistency over time.

The objective is to extract structured insights from raw match data and visualize patterns in:

- Kill / Death performance
- Agent selection frequency
- Match-to-match consistency
- Performance trends over time

***Data Source***

- Match-level Valorant performance data
- Includes:
  - Kills, deaths, assists
  - Agent selection
  - Match outcomes
  - Temporal ordering of matches
Data is cleaned and transformed into analysis-ready formats.

***Analysis Description***

**Performance Metrics**
- Kill/Death (K/D) ratios
- Rolling performance averages
- Match-level performance trends

**Agent Analysis**
- Agent usage frequency
- Performance breakdown by agent
- Comparative agent effectiveness

**Temporal Trends**
- Time-series visualization of performance
- Identification of hot streaks and regressions
- Consistency analysis across matches

***Visualization Outputs***

- K/D ratio trends over matches
- Agent usage distributions
-Performance over time plots
- Comparative performance visualizations

All plots are saved to the figures/ directory.
```bash
Project Structure
Valorant-Project/
│── data/
│   ├── raw/
│   └── processed/
│
│── notebooks/
│   └── analysis.ipynb
│
│── figures/
│   ├── kd_trends.png
│   ├── agent_usage.png
│   └── performance_over_time.png
│
│── src/
│   └── analysis.py
│
│── README.md
│── requirements.txt
```
***Results Interpretation***

- Performance trends highlight periods of improvement and decline
- Agent usage analysis reveals playstyle preferences
- Rolling averages smooth match-to-match variance and expose consistency
This project emphasizes data analysis methodology, not gameplay coaching.

***Analysis***

Match-level Valorant performance data was analyzed to study player consistency, agent usage, and temporal performance trends. Time-series analysis of K/D ratios revealed substantial short-term variance but clear medium-term performance trends when smoothed using rolling averages. K/D was derived to be the most and only correlative individual preformence metric in predicting winrate.

Agent-level analysis showed distinct performance differences across agents, indicating that agent choice plays a measurable role in match outcomes beyond raw mechanical skill. Usage frequency distributions highlighted player preference stability over time, while performance-by-agent comparisons identified agents with higher average impact.

The results demonstrate how match telemetry can be transformed into interpretable performance metrics, enabling objective evaluation of improvement, consistency, and playstyle tendencies over extended match histories.

***Technologies Used***
- Python
  - pandas
  - matplotlib
  - seaborn
- Jupyter Notebooks
