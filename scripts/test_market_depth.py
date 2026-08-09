from src.simulator.market_simulator import MarketSimulator

sim = MarketSimulator()

sim.run(500)

book = sim.matching_engine.order_book

print("Top Bid Levels")
for level in book.top_bid_levels():
    print(level)

print()

print("Top Ask Levels")
for level in book.top_ask_levels():
    print(level)

print()

print("Top-5 Bid Volume:", book.total_bid_volume())
print("Top-5 Ask Volume:", book.total_ask_volume())