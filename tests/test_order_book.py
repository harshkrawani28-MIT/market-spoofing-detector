from src.simulator.order import Order
from src.simulator.order_book import OrderBook


def test_order_book():

    book = OrderBook()

    order1 = Order(
        order_id=1,
        timestamp=0.0,
        event_type="ADD",
        side="BUY",
        price=100.00,
        size=300,
        trader_id=1,
        is_spoof=False,
    )

    order2 = Order(
        order_id=2,
        timestamp=0.0,
        event_type="ADD",
        side="BUY",
        price=100.02,
        size=200,
        trader_id=2,
        is_spoof=False,
    )

    order3 = Order(
        order_id=3,
        timestamp=0.0,
        event_type="ADD",
        side="SELL",
        price=100.05,
        size=500,
        trader_id=3,
        is_spoof=False,
    )

    book.add_order(order1)

    book.add_order(order2)

    book.add_order(order3)

    assert book.best_bid() == 100.02

    assert book.best_ask() == 100.05

    assert book.spread() == 0.03

    assert book.mid_price() == 100.035

    assert book.bid_depth() == 500

    assert book.ask_depth() == 500

    assert book.order_book_imbalance() == 0.0

    book.remove_order(order2)

    assert book.best_bid() == 100.00