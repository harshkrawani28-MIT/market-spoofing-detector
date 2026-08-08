from src.simulator.market_simulator import MarketSimulator

simulator = MarketSimulator()

simulator.run(10)

print(f"Generated {len(simulator.events)} events:\n")

for event in simulator.events:
    print(
        f"{event.event_type:8}"
        f" | ID={event.order_id}"
        f" | {event.side:4}"
        f" | Price={event.price:.2f}"
        f" | Size={event.size}"
        f" | Spoof={event.is_spoof}"
    )

def test_cancel_order():

    simulator = MarketSimulator()

    simulator.add_order()

    assert len(simulator.active_orders) == 1

    simulator.cancel_random_order()

    assert len(simulator.active_orders) == 0

    assert simulator.events[-1].event_type == "CANCEL"