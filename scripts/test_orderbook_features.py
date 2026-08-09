from src.features.orderbook_features import OrderBookFeatures
from src.features.order_book_replayer import OrderBookReplayer
import pandas as pd


df = pd.read_csv("data/raw/market_events.csv")

replayer = OrderBookReplayer()

snapshots = replayer.replay(df)

features = OrderBookFeatures.compute(
    snapshots[100]
)

print(features)