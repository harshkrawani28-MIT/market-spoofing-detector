import pandas as pd

from src.features.feature_engineering import FeatureEngineer


def main():

    df = pd.read_csv(
        "data/raw/market_events.csv"
    )

    engineer = FeatureEngineer(df)

    df = engineer.add_basic_features()
    df = engineer.add_order_lifetime()

    df = engineer.add_order_age()

    df.to_csv(
        "data/processed/features.csv",
        index=False,
    )

    print(df.head())


if __name__ == "__main__":
    main()