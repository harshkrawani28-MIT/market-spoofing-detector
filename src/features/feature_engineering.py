"""
Feature engineering for spoofing detection.
"""

from __future__ import annotations

import pandas as pd


class FeatureEngineer:

    def __init__(self, dataframe: pd.DataFrame):

        self.df = dataframe.copy()

    def add_basic_features(self):

        self.df["is_buy"] = (
            self.df["side"] == "BUY"
        ).astype(int)

        self.df["is_sell"] = (
            self.df["side"] == "SELL"
        ).astype(int)

        self.df["is_add"] = (
            self.df["event_type"] == "ADD"
        ).astype(int)

        self.df["is_cancel"] = (
            self.df["event_type"] == "CANCEL"
        ).astype(int)

        self.df["is_execute"] = (
            self.df["event_type"] == "EXECUTE"
        ).astype(int)

        return self.df

    def add_order_lifetime(self):

        add_times = {}

        lifetime = []

        for _, row in self.df.iterrows():

            order_id = row["order_id"]

            if row["event_type"] == "ADD":

                add_times[order_id] = row["timestamp"]

                lifetime.append(0.0)

            elif order_id in add_times:

                life = (
                    row["timestamp"]
                    -
                    add_times[order_id]
                )

                lifetime.append(round(life, 6))

            else:

                lifetime.append(0.0)

        self.df["order_lifetime"] = lifetime

        return self.df

    def add_order_age(self):

        add_times = {}

        ages = []

        for _, row in self.df.iterrows():

            order_id = row["order_id"]

            if row["event_type"] == "ADD":

                add_times[order_id] = row["timestamp"]

            if order_id in add_times:

                age = row["timestamp"] - add_times[order_id]

            else:

                age = 0.0

            ages.append(round(age, 6))

        self.df["order_age"] = ages

        return self.df