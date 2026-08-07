"""
Abstract trader definition.

Every trader in the simulator must inherit
from this class.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from .order import Order

class Trader(ABC):
    """
    Base class for all market participants.
    """

    def __init__(self, trader_id: int):

        self.trader_id = trader_id

    @abstractmethod
    def create_order(
        self,
        timestamp: float,
        order_id: int,
        current_price: float,
    ) -> Order:
        """
        Create a market order.

        Must be implemented by subclasses.
        """

        pass