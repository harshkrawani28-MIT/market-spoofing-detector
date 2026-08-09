"""
Represents a single price level in the limit order book.
"""

from __future__ import annotations

from collections import deque

from src.simulator.order import Order


class PriceLevel:
    """
    Stores all active orders at one price.

    Orders are maintained in FIFO order,
    matching how most exchanges prioritize
    orders at the same price.
    """

    def __init__(self, price: float):

        self.price = price

        self.orders = deque()

    def add_order(self, order: Order):
        """
        Add an order to the back of the queue.
        """

        self.orders.append(order)

    def remove_order(self, order_id: int):
        """
        Remove a specific order from this price level.

        Returns True if removed.
        Returns False if not found.
        """

        for order in list(self.orders):

            if order.order_id == order_id:

                self.orders.remove(order)

                return True

        return False

    def is_empty(self) -> bool:
        """
        Check whether this price level
        has any remaining orders.
        """

        return len(self.orders) == 0

    def total_volume(self) -> int:
        """
        Total quantity resting
        at this price level.
        """

        return sum(order.size for order in self.orders)

    def order_count(self) -> int:
        """
        Number of active orders
        at this price level.
        """

        return len(self.orders)

    def first_order(self):
        """
        Return the oldest order
        at this price level.

        Returns None if empty.
        """

        if self.orders:

            return self.orders[0]

        return None
    