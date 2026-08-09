"""
Market microstructure feature extraction.
"""

from __future__ import annotations

from typing import Dict

from src.simulator.order import Order


class OrderBookFeatures:
    """
    Computes market microstructure features
    from one order book snapshot.
    """

    @staticmethod
    def compute(snapshot: Dict) -> Dict:

        orders = snapshot["orders"]

        best_bid = snapshot["best_bid"]
        best_ask = snapshot["best_ask"]

        features = {}

        features["best_bid"] = best_bid
        features["best_ask"] = best_ask

        # -----------------------------
        # Mid Price
        # -----------------------------

        if best_bid is not None and best_ask is not None:
            mid_price = (best_bid + best_ask) / 2
        else:
            mid_price = None

        features["mid_price"] = mid_price

        # -----------------------------
        # Bid Ask Spread
        # -----------------------------

        if best_bid is not None and best_ask is not None:
            spread = best_ask - best_bid
        else:
            spread = None

        features["spread"] = spread

        # -----------------------------
        # Market Depth
        # -----------------------------

        bid_depth = 0
        ask_depth = 0

        for order in orders.values():

            if order.side == "BUY":
                bid_depth += order.size

            else:
                ask_depth += order.size

        features["bid_depth"] = bid_depth
        features["ask_depth"] = ask_depth

        # -----------------------------
        # Order Imbalance
        # -----------------------------

        total_depth = bid_depth + ask_depth

        if total_depth == 0:
            imbalance = 0
        else:
            imbalance = (
                bid_depth - ask_depth
            ) / total_depth

        features["imbalance"] = imbalance

        # -----------------------------
        # Number of Orders
        # -----------------------------

        features["num_orders"] = len(orders)

        return features