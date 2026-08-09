from src.features.feature_extractor import FeatureExtractor


def main():

    extractor = FeatureExtractor(
        "data/raw/market_events.csv"
    )

    dataset = extractor.build_dataset()

    dataset.to_csv(
        "data/processed/features.csv",
        index=False,
    )

    print(dataset.head())


if __name__ == "__main__":
    main()