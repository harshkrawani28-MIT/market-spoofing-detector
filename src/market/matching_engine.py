"""
Matching engine for the limit order book.
"""

from __future__ import annotations

from src.simulator.order import Order
from src.features.order_book import OrderBook


class MatchingEngine:

    def __init__(self):

        self.order_book = OrderBook()

    def process_order(self, order: Order):

        """
        Process one incoming order.

        Returns

            ("ADD", order)

        or

            ("EXECUTE", matched_order)
        """

        best_bid = self.order_book.best_bid()

        best_ask = self.order_book.best_ask()

        # BUY order

        if order.side == "BUY":

            if best_ask is not None and order.price >= best_ask:

                return "EXECUTE", order

            self.order_book.add_order(order)

            return "ADD", order

        # SELL order

        if best_bid is not None and order.price <= best_bid:

            return "EXECUTE", order

        self.order_book.add_order(order)

        return "ADD", order