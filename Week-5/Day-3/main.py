import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


chunks = []

for chunk in pd.read_csv("climate_data.csv", chunksize=100000):

    chunk = chunk.dropna(subset=["Temperature", "Timestamp"])


    chunk["Timestamp"] = pd.to_datetime(chunk["Timestamp"])


    chunk["QualityFlag"] = chunk["QualityFlag"].fillna("GOOD")

    chunks.append(chunk)


df = pd.concat(chunks, ignore_index=True)


df.set_index(["Country", "State", "Timestamp"], inplace=True)



rolling_median = (
    df["Temperature"]
    .rolling(window=5, min_periods=1)
    .median()
)

df["Temperature"] = np.where(
    df["QualityFlag"] == "BAD",
    rolling_median,
    df["Temperature"]
)

annual = (
    df["Temperature"]
    .groupby(df.index.get_level_values("Timestamp").year)
    .mean()
)

baseline = annual.mean()

anomaly = annual - baseline

df = df.reset_index()

df["LatitudeBand"] = pd.cut(
    df["Latitude"],
    bins=np.arange(-90, 91, 10)
)

heatmap = df.pivot_table(
    values="Temperature",
    index="LatitudeBand",
    columns=df["Timestamp"].dt.year,
    aggfunc=np.std
)



fig, ax1 = plt.subplots(figsize=(12,6))

ax1.plot(anomaly.index, anomaly.values,
         color="blue",
         marker="o")

ax1.set_xlabel("Year")
ax1.set_ylabel("Temperature Anomaly")

ax2 = plt.axes([0.62,0.18,0.3,0.3])

ax2.imshow(heatmap,
           aspect="auto",
           cmap="hot",
           origin="lower")

ax2.set_title("Std Dev by Latitude")

plt.tight_layout()
plt.show()