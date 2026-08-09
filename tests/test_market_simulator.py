from src.simulator.market_simulator import MarketSimulator


def test_simulator_initialization():

    simulator = MarketSimulator(
        normal_traders=5,
        spoofing_traders=2,
    )

    assert len(simulator.normal_traders) == 5
    assert len(simulator.spoofing_traders) == 2

    assert simulator.current_price == 100.0
    assert simulator.next_order_id == 100001

    assert simulator.active_orders == {}
    assert simulator.events == []


def test_simulation_step():

    simulator = MarketSimulator()

    simulator.add_order()

    # Sometimes the chosen trader is a spoofer who decides
    # not to spoof this round.
    # Therefore 0 or 1 events are both valid.

    assert len(simulator.events) in (0, 1)

    if simulator.events:

        assert len(simulator.active_orders) == 1
        assert simulator.next_order_id == 100002


def test_run():

    simulator = MarketSimulator()

    simulator.run(20)

    # We may generate fewer than 20 events because
    # spoofers sometimes intentionally skip placing
    # a spoof order.

    assert 0 <= len(simulator.events) <= 20

    # Verify timestamps always increase.

    timestamps = [e.timestamp for e in simulator.events]

    assert timestamps == sorted(timestamps)


def test_execute_order():

    simulator = MarketSimulator()

    # Keep adding until an order actually exists.
    while len(simulator.active_orders) == 0:
        simulator.add_order()

    assert len(simulator.active_orders) == 1

    simulator.execute_random_order()

    assert len(simulator.active_orders) == 0

    assert simulator.events[-1].event_type == "EXECUTE"