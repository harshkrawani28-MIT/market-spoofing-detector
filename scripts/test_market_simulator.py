from src.simulator.market_simulator import MarketSimulator

simulator = MarketSimulator()

simulator.run(10)

print(f"Generated {len(simulator.events)} events:\n")

for event in simulator.events:
    print(event)