"""
Order data model.

Represents one market event in the synthetic
Limit Order Book simulator.
"""

from dataclasses import dataclass

@dataclass
class Order:
    """
    Represents a single order book event.
    """

    order_id: int

    timestamp: float

    event_type: str

    side: str

    price: float

    size: int

    trader_id: int

    is_spoof: bool


    def __post_init__(self) -> None:
          """
          Validate order fields after initialization.
          """

          if self.side not in ("BUY", "SELL"):
            raise ValueError(f"Invalid side: {self.side}")

          if self.event_type not in ("ADD", "CANCEL", "EXECUTE"):
            raise ValueError(f"Invalid event type: {self.event_type}")

          if self.price <= 0:
            raise ValueError("Price must be positive.")

          if self.size <= 0:
            raise ValueError("Size must be positive.")
