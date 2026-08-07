"""
Implementation of a spoofing market participant.
"""

from __future__ import annotations

import random

from .order import Order
from .trader import Trader


class SpoofingTrader(Trader):
    """
    Simulates a market participant
    that generates spoofing orders.
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
        Spoofers place unusually
        large orders.
        """

        sizes = [
            5000,
            10000,
            15000,
            20000
        ]

        weights = [
            20,
            35,
            30,
            15
        ]

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
        Spoofers place orders
        very close to the best price.
        """

        offset = random.uniform(-0.01, 0.01)

        return round(current_price + offset, 2)

    def create_order(
        self,
        timestamp: float,
        order_id: int,
        current_price: float,
    ) -> Order:
        """
        Create a spoofing order.
        """

        return Order(
            order_id=order_id,
            timestamp=timestamp,
            event_type="ADD",
            side=self.choose_side(),
            price=self.choose_price(current_price),
            size=self.choose_order_size(),
            trader_id=self.trader_id,
            is_spoof=True,
        )