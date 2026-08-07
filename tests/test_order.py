from src.simulator.order import Order


def test_create_order():

    order = Order(
        order_id=100001,
        timestamp=0.000001,
        event_type="ADD",
        side="BUY",
        price=100.25,
        size=500,
        trader_id=1,
        is_spoof=False,
    )

    assert order.order_id == 100001
    assert order.side == "BUY"
    assert order.price == 100.25