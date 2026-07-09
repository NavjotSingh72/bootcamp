import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("urban_traffic.csv")

df["Timestamp"] = pd.to_datetime(df["Timestamp"])


R = 6371

df["PrevLat"] = df.groupby("VehicleID")["Latitude"].shift()
df["PrevLon"] = df.groupby("VehicleID")["Longitude"].shift()

lat1 = np.radians(df["PrevLat"])
lon1 = np.radians(df["PrevLon"])
lat2 = np.radians(df["Latitude"])
lon2 = np.radians(df["Longitude"])

dlat = lat2 - lat1
dlon = lon2 - lon1

a = np.sin(dlat/2)**2 + np.cos(lat1)*np.cos(lat2)*np.sin(dlon/2)**2
c = 2*np.arcsin(np.sqrt(a))

df["Distance_km"] = R * c


df["GridLat"] = df["Latitude"].round(2)
df["GridLon"] = df["Longitude"].round(2)

traffic = df.groupby(["GridLat","GridLon"]).size()

bins = [0,10,30,100]
labels = ["Gridlock","Slow","Free Flow"]

df["TrafficState"] = pd.cut(df["Speed"],
                            bins=bins,
                            labels=labels,
                            include_lowest=True)


df["Acceleration"] = df.groupby("VehicleID")["Speed"].diff()

print(df)


plt.figure(figsize=(8,6))

plt.scatter(df["Longitude"],
            df["Latitude"],
            c=df["Speed"],
            cmap="RdYlGn",
            s=100)

plt.colorbar(label="Speed")

plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Traffic Congestion")

plt.show()


df["Day"] = df["Timestamp"].dt.day_name()

avg_speed = df.groupby("Day")["Speed"].mean()

categories = avg_speed.index.tolist()
values = avg_speed.values.tolist()

values += values[:1]

angles = np.linspace(0,2*np.pi,len(categories),endpoint=False).tolist()
angles += angles[:1]

fig = plt.figure(figsize=(6,6))
ax = plt.subplot(111, polar=True)

ax.plot(angles, values)
ax.fill(angles, values, alpha=0.25)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)

plt.title("Average Speed by Day")

plt.show()