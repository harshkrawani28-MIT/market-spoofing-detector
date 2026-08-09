"""
Limit Order Book implementation.
"""

from __future__ import annotations

from .price_level import PriceLevel


class OrderBook:
    """
    Multi-level Limit Order Book.

    Keeps bids and asks separated by price level.
    """

    def __init__(self):

        self.bids = {}

        self.asks = {}

    def add_order(self, order):
        """
        Insert an order into the book.
        """

        if order.side == "BUY":

            if order.price not in self.bids:
                self.bids[order.price] = PriceLevel(order.price)

            self.bids[order.price].add_order(order)

        else:

            if order.price not in self.asks:
                self.asks[order.price] = PriceLevel(order.price)

            self.asks[order.price].add_order(order)

    def remove_order(self, order):
        """
        Remove an order from the book.
        """

        if order.side == "BUY":
            level = self.bids.get(order.price)
        else:
            level = self.asks.get(order.price)

        if level is None:
            return

        level.remove_order(order.order_id)

        if level.is_empty():

            if order.side == "BUY":
                del self.bids[order.price]
            else:
                del self.asks[order.price]

    def best_bid(self):
        """
        Highest resting bid.
        """

        if not self.bids:
            return None

        return max(self.bids.keys())

    def best_ask(self):
        """
        Lowest resting ask.
        """

        if not self.asks:
            return None

        return min(self.asks.keys())

    def bid_depth(self):
        """
        Total resting BUY volume.
        """

        return sum(
            level.total_volume()
            for level in self.bids.values()
        )

    def ask_depth(self):
        """
        Total resting SELL volume.
        """

        return sum(
            level.total_volume()
            for level in self.asks.values()
        )

    def spread(self):
        """
        Bid-ask spread.
        """

        bid = self.best_bid()
        ask = self.best_ask()

        if bid is None or ask is None:
            return None

        return ask - bid

    def mid_price(self):
        """
        Mid-price.
        """

        bid = self.best_bid()
        ask = self.best_ask()

        if bid is None or ask is None:
            return None

        return (bid + ask) / 2
    
    def top_bid_levels(self, levels=5):
     """
     Return top N bid price levels.

     Highest prices first.
     """

     prices = sorted(
        self.bids.keys(),
        reverse=True
     )[:levels]

     result = []

     for price in prices:

        level = self.bids[price]

        result.append(
            (
                price,
                level.total_volume(),
                level.order_count(),
            )
         )

     return result


    def top_ask_levels(self, levels=5):
     """
     Return top N ask price levels.

     Lowest prices first.
     """

     prices = sorted(
        self.asks.keys()
     )[:levels]

     result = []

     for price in prices:

        level = self.asks[price]

        result.append(
            (
                price,
                level.total_volume(),
                level.order_count(),
            )
         )

     return result


    def total_bid_volume(self, levels=5):
     """
     Total volume across the
     first N bid levels.
     """

     return sum(
        volume
        for _, volume, _
        in self.top_bid_levels(levels)
     )


    def total_ask_volume(self, levels=5):
     """
     Total volume across the
     first N ask levels.
     """

     return sum(
        volume
        for _, volume, _
        in self.top_ask_levels(levels)
     )