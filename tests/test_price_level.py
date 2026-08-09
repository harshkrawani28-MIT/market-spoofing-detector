from src.features.price_level import PriceLevel
from src.simulator.order import Order


def make_order(order_id, size):

    return Order(
        order_id=order_id,
        timestamp=0.0,
        event_type="ADD",
        side="BUY",
        price=100.0,
        size=size,
        trader_id=1,
        is_spoof=False,
    )


def test_add_order():

    level = PriceLevel(100.0)

    level.add_order(make_order(1, 200))

    assert level.order_count() == 1

    assert level.total_volume() == 200


def test_fifo():

    level = PriceLevel(100.0)

    level.add_order(make_order(1, 100))

    level.add_order(make_order(2, 300))

    assert level.first_order().order_id == 1


def test_remove():

    level = PriceLevel(100.0)

    level.add_order(make_order(1, 100))

    level.add_order(make_order(2, 300))

    assert level.remove_order(1)

    assert level.first_order().order_id == 2


def test_empty():

    level = PriceLevel(100.0)

    level.add_order(make_order(1, 100))

    level.remove_order(1)

    assert level.is_empty()