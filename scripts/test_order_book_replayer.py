import pandas as pd

from src.features.order_book_replayer import OrderBookReplayer

df = pd.read_csv(
    "data/raw/market_events.csv"
)

replayer = OrderBookReplayer()

snapshots = replayer.replay(df)

print("Snapshots:", len(snapshots))
print()

print("First Snapshot")
print(snapshots[0])
print()

print("Snapshot 100")
print(snapshots[100])