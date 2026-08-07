""" 
Synthetic Limit Order Book (LOB) Data Generator

This script generates synthetic high-frequency trading events that resemble LOBSTER-style market data.

Author: Harsh Rawani
Project: High-Frequency Market Microstructure Anomaly and Spoofing Detector
"""
from pathlib import Path
import random

import numpy as np
import pandas as pd

NUM_EVENTS = 50_000

BASE_PRICE = 100.00

OUTPUT_FILE = (
    Path(__file__).resolve().parent.parent
    /"data"
    /"raw"
    /"synthetic_lob.csv"
)


# -------------------------------
# Helper Functions
# -------------------------------

def generate_timestamp(event_number: int) -> float:
    """
    Generate a synthetic timestamp.

    Each event occurs one microsecond after the previous event.

    Parameters
    ----------
    event_number : int
        Sequential event number.

    Returns
    -------
    float
        Timestamp in seconds.
    """

    return event_number * 0.000001

def choose_event_type() -> str:
    """
    Randomly choose a market event.

    Returns
    -------
    str
        One of:
        - ADD
        - CANCEL
        - EXECUTE
    """

    return random.choices(
        population=["ADD", "CANCEL", "EXECUTE"],
        weights=[70, 20, 10],
        k=1
    )[0]

def choose_side() -> str:
    """
    Randomly choose whether an order
    is BUY or SELL.
    """

    return random.choice(["BUY", "SELL"])

def generate_order_size() -> int:
    """
    Generate a realistic order size.

    Small orders are common.

    Large orders occur occasionally.
    """

    possible_sizes = [
        100,
        200,
        300,
        500,
        1000,
        1500,
        2500,
        5000,
        10000
    ]

    weights = [
        30,
        25,
        15,
        10,
        8,
        5,
        3,
        2,
        2
    ]

    return random.choices(
        possible_sizes,
        weights=weights,
        k=1
    )[0]

def generate_price(current_price: float) -> float:
    """
    Generate the next market price using
    a simple random walk.

    Parameters
    ----------
    current_price : float
        Current market price.

    Returns
    -------
    float
        Updated market price.
    """

    price_change = random.uniform(-0.05, 0.05)

    new_price = current_price + price_change

    return round(new_price, 2)

def generate_events() -> pd.DataFrame:
    """
    Generate a synthetic stream of
    Limit Order Book events.

    Returns
    -------
    pandas.DataFrame
        DataFrame containing all events.
    """

    events = []

    active_orders = {}

    current_price = BASE_PRICE

    next_order_id = 100000

if __name__ == "__main__":

    print("Timestamp:")
    print(generate_timestamp(5))

    print()

    print("Random Events")

    for _ in range(10):
        print(choose_event_type())

    print()

    print("Random Sides")

    for _ in range(10):
        print(choose_side())

    print()

    print("Random Sizes")

    for _ in range(10):
        print(generate_order_size())
