import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("orders.csv")

df["Timestamp"] = pd.to_datetime(df["Timestamp"])

df = df.sort_values("Timestamp")

def calculate_vwap(group):
    return (group["Price"] * group["Volume"]).sum() / group["Volume"].sum()

vwap = (
    df.groupby(
        [
            "Ticker",
            pd.Grouper(key="Timestamp", freq="5min")
        ]
    )
    .apply(calculate_vwap)
    .reset_index(name="VWAP")
)

print(vwap)

spread = []

for (ticker, time), group in df.groupby(
    ["Ticker", pd.Grouper(key="Timestamp", freq="5min")]
):

    buy = group[group["Action"]=="BUY"]["Price"]
    sell = group[group["Action"]=="SELL"]["Price"]

    if len(buy)>0 and len(sell)>0:

        bid = buy.max()

        ask = sell.min()

        spread.append([ticker,time,bid,ask,ask-bid])

spread = pd.DataFrame(
    spread,
    columns=["Ticker","Time","Bid","Ask","Spread"]
)

print(spread)

prices = np.sort(df["Price"].unique())

depth = np.searchsorted(prices, df["Price"])

df["MarketDepth"] = depth

print(df.head())

ohlc = (
    df.set_index("Timestamp")
      .groupby("Ticker")["Price"]
      .resample("5min")
      .ohlc()
)

print(ohlc)

volume = (
    df.set_index("Timestamp")
      .groupby("Ticker")["Volume"]
      .resample("5min")
      .sum()
)

ticker = "AAPL"

price = df[df["Ticker"]==ticker]

plt.figure(figsize=(12,6))

plt.plot(price["Timestamp"],
         price["Price"],
         label="Price")

plt.plot(vwap[vwap["Ticker"]==ticker]["Timestamp"],
         vwap[vwap["Ticker"]==ticker]["VWAP"],
         color="red",
         linewidth=2,
         label="VWAP")

plt.xlabel("Time")
plt.ylabel("Price")

plt.title("Price vs VWAP")

plt.legend()

plt.show()

vol = volume.loc[ticker]

plt.figure(figsize=(12,4))

plt.bar(vol.index,
        vol.values)

plt.title("Volume Spikes")

plt.xlabel("Time")

plt.ylabel("Volume")

plt.show()