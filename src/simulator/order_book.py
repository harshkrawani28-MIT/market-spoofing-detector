"""
Multi-level Limit Order Book.
"""

from __future__ import annotations

from collections import defaultdict

from .order import Order


class OrderBook:
    """
    Stores BUY and SELL orders
    organized by price level.
    """

    def __init__(self):

        self.bid_book = defaultdict(list)

        self.ask_book = defaultdict(list)

    def add_order(self, order: Order):

        if order.side == "BUY":
            self.bid_book[order.price].append(order)

        else:
            self.ask_book[order.price].append(order)

    def remove_order(self, order: Order):

        if order.side == "BUY":

            book = self.bid_book

        else:

            book = self.ask_book

        if order.price not in book:
            return

        book[order.price] = [
            existing
            for existing in book[order.price]
            if existing.order_id != order.order_id
        ]

        if len(book[order.price]) == 0:
            del book[order.price]

    def best_bid(self):

        if not self.bid_book:
            return None

        return max(self.bid_book.keys())

    def best_ask(self):

        if not self.ask_book:
            return None

        return min(self.ask_book.keys())

    def spread(self):

        bid = self.best_bid()

        ask = self.best_ask()

        if bid is None or ask is None:
            return None

        return round(ask - bid, 4)

    def mid_price(self):

        bid = self.best_bid()

        ask = self.best_ask()

        if bid is None or ask is None:
            return None

        return round((bid + ask) / 2, 4)

    def bid_depth(self):

        return sum(
            order.size
            for orders in self.bid_book.values()
            for order in orders
        )

    def ask_depth(self):

        return sum(
            order.size
            for orders in self.ask_book.values()
            for order in orders
        )

    def order_book_imbalance(self):

        bid = self.bid_depth()

        ask = self.ask_depth()

        total = bid + ask

        if total == 0:
            return 0.0

        return round((bid - ask) / total, 6)