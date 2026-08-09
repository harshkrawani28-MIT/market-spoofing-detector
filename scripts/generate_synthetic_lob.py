from src.simulator.market_simulator import MarketSimulator


def main():

    simulator = MarketSimulator()

    simulator.run(10000)

    simulator.export_events_to_csv(
        "data/raw/market_events.csv"
    )

    print("Simulation completed.")

    print(f"Generated {len(simulator.events)} events.")

    print("CSV saved to:")

    print("data/raw/market_events.csv")


if __name__ == "__main__":
    main()