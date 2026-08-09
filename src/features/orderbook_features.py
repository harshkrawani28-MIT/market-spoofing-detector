"""
Market microstructure feature extraction.
"""

from __future__ import annotations

from typing import Dict


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

        # -------------------------------------------------
        # Best Prices
        # -------------------------------------------------

        features["best_bid"] = best_bid
        features["best_ask"] = best_ask

        # -------------------------------------------------
        # Mid Price
        # -------------------------------------------------

        if best_bid is not None and best_ask is not None:
            features["mid_price"] = (best_bid + best_ask) / 2
        else:
            features["mid_price"] = None

        # -------------------------------------------------
        # Bid Ask Spread
        # -------------------------------------------------

        if best_bid is not None and best_ask is not None:
            features["spread"] = best_ask - best_bid
        else:
            features["spread"] = None

        # -------------------------------------------------
        # Market Depth
        # -------------------------------------------------

        bid_depth = 0
        ask_depth = 0

        bid_levels = {}
        ask_levels = {}

        for order in orders.values():

            if order.side == "BUY":

                bid_depth += order.size

                bid_levels.setdefault(order.price, 0)
                bid_levels[order.price] += order.size

            else:

                ask_depth += order.size

                ask_levels.setdefault(order.price, 0)
                ask_levels[order.price] += order.size

        features["bid_depth"] = bid_depth
        features["ask_depth"] = ask_depth

        # -------------------------------------------------
        # Overall Order Book Imbalance
        # -------------------------------------------------

        total_depth = bid_depth + ask_depth

        if total_depth == 0:
            imbalance = 0.0
        else:
            imbalance = (bid_depth - ask_depth) / total_depth

        features["imbalance"] = imbalance

        # -------------------------------------------------
        # Top-5 Bid Volume
        # -------------------------------------------------

        top5_bid = 0

        for price in sorted(
            bid_levels.keys(),
            reverse=True
        )[:5]:

            top5_bid += bid_levels[price]

        # -------------------------------------------------
        # Top-5 Ask Volume
        # -------------------------------------------------

        top5_ask = 0

        for price in sorted(
            ask_levels.keys()
        )[:5]:

            top5_ask += ask_levels[price]

        features["top5_bid_volume"] = top5_bid
        features["top5_ask_volume"] = top5_ask

        # -------------------------------------------------
        # Top-5 Order Book Imbalance
        # -------------------------------------------------

        if top5_bid + top5_ask == 0:
            top5_imbalance = 0.0
        else:
            top5_imbalance = (
                top5_bid - top5_ask
            ) / (
                top5_bid + top5_ask
            )

        features["top5_imbalance"] = top5_imbalance

        # -------------------------------------------------
        # Number of Orders
        # -------------------------------------------------

        features["num_orders"] = len(orders)

        return features