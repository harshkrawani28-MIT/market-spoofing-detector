"""
Core market simulator.
"""

from __future__ import annotations

from .normal_trader import NormalTrader
from .spoofing_trader import SpoofingTrader
import random

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

    def add_order(self):
     """
     Create one new order and add it
     to the active order book.
     """

     all_traders = (
        self.normal_traders +
        self.spoofing_traders
     )

     trader = random.choice(all_traders)

     self.current_timestamp += random.uniform(
        0.0001,
        0.001,
     )

     order = trader.create_order(
        timestamp=round(self.current_timestamp, 6),
        order_id=self.next_order_id,
        current_price=self.current_price,
     )

     self.active_orders[order.order_id] = order

     self.events.append(order)

     self.next_order_id += 1 

    def step(self):
     """
     Execute one simulation step.
     """

     self.add_order()

    def run(self, num_steps: int):
     """
     Run the simulation.
     """

     for _ in range(num_steps):
        self.step()