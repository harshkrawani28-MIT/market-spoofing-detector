"""
Core market simulator.
"""

from __future__ import annotations

import csv
import random

from .normal_trader import NormalTrader
from .spoofing_trader import SpoofingTrader
from .order import Order


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

    def _remove_order(self, event_type: str):
        """
        Remove one random active order and
        record the event.
        """

        if not self.active_orders:
            return

        order_id = random.choice(
            list(self.active_orders.keys())
        )

        order = self.active_orders.pop(order_id)

        self.current_timestamp += random.uniform(
            0.0001,
            0.001,
        )

        event = Order(
            order_id=order.order_id,
            timestamp=round(self.current_timestamp, 6),
            event_type=event_type,
            side=order.side,
            price=order.price,
            size=order.size,
            trader_id=order.trader_id,
            is_spoof=order.is_spoof,
        )

        self.events.append(event)

    def cancel_random_order(self):
        """
        Cancel one random active order.
        """

        self._remove_order("CANCEL")

    def execute_random_order(self):
        """
        Execute one random active order.
        """

        self._remove_order("EXECUTE")

    def resolve_random_order(self):
        """
        Resolve one active order.

        Spoof orders are usually cancelled.

        Normal orders are usually executed.
        """

        if not self.active_orders:
            return

        order = random.choice(
            list(self.active_orders.values())
        )

        if order.is_spoof:

            outcome = random.random()

            if outcome < 0.90:
                self._remove_specific_order(
                    order.order_id,
                    "CANCEL"
                )

            elif outcome < 0.95:
                self._remove_specific_order(
                    order.order_id,
                    "EXECUTE"
                )

            else:
                pass

        else:

            outcome = random.random()

            if outcome < 0.70:
                self._remove_specific_order(
                    order.order_id,
                    "EXECUTE"
                )

            elif outcome < 0.90:
                self._remove_specific_order(
                    order.order_id,
                    "CANCEL"
                )

            else:
                pass

    def _remove_specific_order(
        self,
        order_id: int,
        event_type: str,
    ):
        """
        Remove a specific order.
        """

        if order_id not in self.active_orders:
            return

        order = self.active_orders.pop(order_id)

        self.current_timestamp += random.uniform(
            0.0001,
            0.001,
        )

        event = Order(
            order_id=order.order_id,
            timestamp=round(
                self.current_timestamp,
                6,
            ),
            event_type=event_type,
            side=order.side,
            price=order.price,
            size=order.size,
            trader_id=order.trader_id,
            is_spoof=order.is_spoof,
        )

        self.events.append(event)

    def step(self):
        """
        Execute one simulation step.
        """

        if not self.active_orders:
            self.add_order()
            return

        action = random.random()

        if action < 0.70:

            self.add_order()

        else:

            self.resolve_random_order()

    def run(self, num_steps: int):
        """
        Run the simulation.
        """

        for _ in range(num_steps):
            self.step()

    def export_events_to_csv(self, filename):
        """
        Export events to CSV.
        """

        with open(
            filename,
            mode="w",
            newline="",
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "order_id",
                "timestamp",
                "event_type",
                "side",
                "price",
                "size",
                "trader_id",
                "is_spoof",
            ])

            for event in self.events:

                writer.writerow([
                    event.order_id,
                    event.timestamp,
                    event.event_type,
                    event.side,
                    event.price,
                    event.size,
                    event.trader_id,
                    event.is_spoof,
                ])