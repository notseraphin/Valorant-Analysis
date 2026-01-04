import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def logistic_analysis(df):
    features = df[["hs_percent", "kd_ratio", "total_engagements"]].fillna(0)
    target = df["win"].fillna(0)
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
    model = LogisticRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    results = {
        "accuracy": accuracy_score(y_test, y_pred),
        "confusion_matrix": confusion_matrix(y_test, y_pred),
        "classification_report": classification_report(y_test, y_pred, output_dict=True),
        "feature_importance": pd.DataFrame({"feature": features.columns, "coefficient": model.coef_[0]})
    }
    return results

def kd_win_curve(df, targets=[0.5, 0.6, 0.7]):
    df_clean = df.dropna(subset=["kd_ratio", "win"])
    X = df_clean[["kd_ratio"]]
    y = df_clean["win"]
    model = LogisticRegression()
    model.fit(X, y)
    curves = {}
    a = model.coef_[0][0]
    b = model.intercept_[0]
    for t in targets:
        curves[t] = (np.log(t / (1 - t)) - b) / a
    return curves
