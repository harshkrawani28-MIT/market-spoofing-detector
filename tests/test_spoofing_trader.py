from src.simulator.spoofing_trader import SpoofingTrader


def test_create_spoof_order():

    trader = SpoofingTrader(trader_id=999)

    order = trader.create_order(
        timestamp=0.000001,
        order_id=999001,
        current_price=100.00,
    )

    assert order.is_spoof is True
    assert order.size >= 5000
    assert order.event_type == "ADD"