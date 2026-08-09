"""
Feature engineering pipeline.

Converts raw simulator events into
machine-learning features.
"""

from __future__ import annotations

import pandas as pd


class FeatureEngineer:

    def __init__(self, csv_path: str):

        self.csv_path = csv_path

        self.df = pd.read_csv(csv_path)

    def create_features(self):

        """
        Placeholder.

        Feature columns will be added here.
        """

        return self.df

    def save(self, output_path: str):

        self.df.to_csv(
            output_path,
            index=False,
        )