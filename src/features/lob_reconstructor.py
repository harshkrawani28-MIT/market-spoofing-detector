"""
Reconstruct a limit order book from
the generated event stream.
"""

from __future__ import annotations

import csv

from src.simulator.order import Order
from src.simulator.order_book import OrderBook


class LOBReconstructor:
    """
    Reads market events and rebuilds
    the order book event by event.
    """

    def __init__(self):

        self.book = OrderBook()

    def process_event(self, row):

        event = Order(
            order_id=int(row["order_id"]),
            timestamp=float(row["timestamp"]),
            event_type=row["event_type"],
            side=row["side"],
            price=float(row["price"]),
            size=int(row["size"]),
            trader_id=int(row["trader_id"]),
            is_spoof=row["is_spoof"] == "True",
        )

        if event.event_type == "ADD":
            self.book.add_order(event)

        elif event.event_type == "CANCEL":
            self.book.cancel_order(event.order_id)

        elif event.event_type == "EXECUTE":
            self.book.execute_order(event.order_id)

    def reconstruct(self, csv_file):

        with open(csv_file, newline="") as file:

            reader = csv.DictReader(file)

            for row in reader:
                self.process_event(row)