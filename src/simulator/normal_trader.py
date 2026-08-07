"""
Implementation of a normal market participant.
"""

from __future__ import annotations

import random

from .order import Order
from .trader import Trader


class NormalTrader(Trader):
    """
    Simulates a normal market participant.
    """

    def __init__(self, trader_id: int):
        super().__init__(trader_id)

    def choose_side(self) -> str:
        """
        Randomly choose BUY or SELL.
        """
        return random.choice(["BUY", "SELL"])

    def choose_order_size(self) -> int:
        """
        Normal traders mostly place
        small orders.
        """

        sizes = [100, 200, 300, 500, 1000]

        weights = [35, 30, 20, 10, 5]

        return random.choices(
            sizes,
            weights=weights,
            k=1
        )[0]

    def choose_price(
        self,
        current_price: float,
    ) -> float:
        """
        Choose a price close to the
        current market price.
        """

        offset = random.uniform(-0.05, 0.05)

        return round(current_price + offset, 2)

    def create_order(
        self,
        timestamp: float,
        order_id: int,
        current_price: float,
    ) -> Order:
        """
        Create a realistic market order.
        """

        return Order(
            order_id=order_id,
            timestamp=timestamp,
            event_type="ADD",
            side=self.choose_side(),
            price=self.choose_price(current_price),
            size=self.choose_order_size(),
            trader_id=self.trader_id,
            is_spoof=False,
        )