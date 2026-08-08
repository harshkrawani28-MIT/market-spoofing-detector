"""
Core market simulator.
"""

from __future__ import annotations

from .normal_trader import NormalTrader
from .spoofing_trader import SpoofingTrader


class MarketSimulator:
    """
    Simulates a limit order market.
    """

    def __init__(
        self,
        normal_traders: int = 10,
        spoofing_traders: int = 1,
        initial_price: float = 100.0,
    ):

        self.current_price = initial_price

        self.current_timestamp = 0.0

        self.next_order_id = 100001

        self.active_orders = {}

        self.events = []

        self.normal_traders = [
            NormalTrader(i + 1)
            for i in range(normal_traders)
        ]

        self.spoofing_traders = [
            SpoofingTrader(
                normal_traders + i + 1
            )
            for i in range(spoofing_traders)
        ]