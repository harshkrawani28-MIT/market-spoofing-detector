"""
Replay market events to reconstruct
the order book over time.
"""

from __future__ import annotations

import pandas as pd


class OrderBookReplayer:

    def __init__(self):

        self.active_orders = {}

    def process_event(self, row):

        order_id = row["order_id"]

        event = row["event_type"]

        if event == "ADD":

            self.active_orders[order_id] = row

        elif event in ("CANCEL", "EXECUTE"):

            self.active_orders.pop(order_id, None)

    def best_bid(self):

        bids = [
            order["price"]
            for order in self.active_orders.values()
            if order["side"] == "BUY"
        ]

        if not bids:
            return None

        return max(bids)

    def best_ask(self):

        asks = [
            order["price"]
            for order in self.active_orders.values()
            if order["side"] == "SELL"
        ]

        if not asks:
            return None

        return min(asks)

    def replay(self, dataframe):

        snapshots = []

        for _, row in dataframe.iterrows():

            self.process_event(row)

            snapshots.append(
                {
                    "orders": dict(self.active_orders),
                    "best_bid": self.best_bid(),
                    "best_ask": self.best_ask(),
                }
            )

        return snapshots