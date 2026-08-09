from src.simulator.market_simulator import MarketSimulator

sim = MarketSimulator()

sim.run(100)

print("Best Bid :", sim.best_bid())
print("Best Ask :", sim.best_ask())
print("Spread   :", sim.spread())
print("Mid Price:", sim.mid_price())
print("OBI      :", sim.order_book_imbalance())