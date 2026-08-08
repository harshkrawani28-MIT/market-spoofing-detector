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
    def step(self):
     """
     Execute one simulation step.
     """

    # Choose a trader randomly
     all_traders = (
        self.normal_traders +
        self.spoofing_traders
     )

     trader = random.choice(all_traders)

    # Advance simulated time
     self.current_timestamp += random.uniform(
        0.0001,
        0.001,
     )

    # Ask trader to create an order
     order = trader.create_order(
        timestamp=round(self.current_timestamp, 6),
        order_id=self.next_order_id,
        current_price=self.current_price,
     )

    # Store active order
     self.active_orders[
        order.order_id
     ] = order

    # Store event history
     self.events.append(order)

    # Prepare next order ID
     self.next_order_id += 1    

    def run(self, num_steps: int):
     """
     Run the simulation.
     """

     for _ in range(num_steps):
        self.step()