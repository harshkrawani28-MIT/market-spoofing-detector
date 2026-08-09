"""
Feature engineering for spoofing detection.
"""

from __future__ import annotations

import pandas as pd


class FeatureExtractor:

    def __init__(self, csv_file: str):

        self.df = pd.read_csv(csv_file)

    def cancellation_ratio(self):

        grouped = self.df.groupby("order_id")

        ratios = []

        for order_id, group in grouped:

            added = (group.event_type == "ADD").sum()

            cancelled = (group.event_type == "CANCEL").sum()

            executed = (group.event_type == "EXECUTE").sum()

            ratios.append(
                {
                    "order_id": order_id,
                    "cancelled": cancelled,
                    "executed": executed,
                    "cancel_ratio": cancelled / max(1, added),
                }
            )

        return pd.DataFrame(ratios)

    def lifetime(self):

        grouped = self.df.groupby("order_id")

        rows = []

        for order_id, group in grouped:

            add = group[group.event_type == "ADD"]

            end = group[
                group.event_type.isin(
                    ["CANCEL", "EXECUTE"]
                )
            ]

            if len(add) == 0 or len(end) == 0:
                continue

            lifetime = (
                end.timestamp.iloc[0]
                - add.timestamp.iloc[0]
            )

            rows.append(
                {
                    "order_id": order_id,
                    "lifetime": lifetime,
                }
            )

        return pd.DataFrame(rows)

    def size_features(self):

        adds = self.df[
            self.df.event_type == "ADD"
        ]

        return adds[
            [
                "order_id",
                "size",
                "price",
                "side",
                "trader_id",
                "is_spoof",
            ]
        ]

    def build_dataset(self):

        size = self.size_features()

        cancel = self.cancellation_ratio()

        lifetime = self.lifetime()

        dataset = size.merge(
            cancel,
            on="order_id",
            how="left",
        )

        dataset = dataset.merge(
            lifetime,
            on="order_id",
            how="left",
        )

        dataset.fillna(0, inplace=True)

        return dataset