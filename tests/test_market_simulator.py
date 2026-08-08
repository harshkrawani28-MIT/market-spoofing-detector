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

    assert len(simulator.active_orders) == 1

    assert len(simulator.events) == 1

    assert simulator.next_order_id == 100002

def test_run():

    simulator = MarketSimulator()

    simulator.run(20)

    assert len(simulator.events) == 20

def test_execute_order():

    simulator = MarketSimulator()

    simulator.add_order()

    assert len(simulator.active_orders) == 1

    simulator.execute_random_order()

    assert len(simulator.active_orders) == 0

    assert simulator.events[-1].event_type == "EXECUTE"