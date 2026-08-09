from src.preprocessing.feature_engineering import FeatureEngineer


def main():

    engineer = FeatureEngineer(
        "data/raw/market_events.csv"
    )

    engineer.create_features()

    engineer.save(
        "data/processed/features.csv"
    )

    print("Feature engineering complete.")
    print("Saved:")
    print("data/processed/features.csv")


if __name__ == "__main__":
    main()