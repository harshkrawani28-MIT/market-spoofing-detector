"""
Train a baseline Random Forest spoofing detector.
"""

from __future__ import annotations

import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split


def main():

    df = pd.read_csv(
        "data/processed/features.csv"
    )

    df["side"] = df["side"].map(
        {
            "BUY": 0,
            "SELL": 1,
        }
    )

    X = df.drop(
        columns=[
            "order_id",
            "is_spoof",
        ]
    )

    y = df["is_spoof"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y,
    )

    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42,
    )

    model.fit(
        X_train,
        y_train,
    )

    predictions = model.predict(
        X_test
    )

    print()

    print("Classification Report")

    print()

    print(
        classification_report(
            y_test,
            predictions,
        )
    )


if __name__ == "__main__":
    main()