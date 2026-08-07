from src.simulator.normal_trader import NormalTrader


def test_create_normal_order():

    trader = NormalTrader(trader_id=1)

    order = trader.create_order(
        timestamp=0.000001,
        order_id=100001,
        current_price=100.00,
    )

    assert order.trader_id == 1
    assert order.is_spoof is False
    assert order.event_type == "ADD"
    assert order.side in ("BUY", "SELL")
    assert order.size > 0