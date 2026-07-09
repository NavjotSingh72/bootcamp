import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("ecommerce_data.csv")


df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])


df["Revenue"] = df["Quantity"] * df["UnitPrice"]



df["InvoiceMonth"] = df["InvoiceDate"].dt.to_period("M")

df["CohortMonth"] = df.groupby("CustomerID")["InvoiceMonth"].transform("min")



df["CohortIndex"] = (
    (df["InvoiceMonth"].dt.year - df["CohortMonth"].dt.year) * 12 +
    (df["InvoiceMonth"].dt.month - df["CohortMonth"].dt.month) + 1
)



cohort_data = df.groupby(
    ["CohortMonth","CohortIndex"]
)["CustomerID"].nunique().reset_index()

cohort_counts = cohort_data.pivot(
    index="CohortMonth",
    columns="CohortIndex",
    values="CustomerID"
)

cohort_size = cohort_counts.iloc[:,0]

retention = cohort_counts.divide(cohort_size, axis=0) * 100

print("\nRetention Matrix (%)")
print(retention.round(1))



decay = retention.diff(axis=1)

print("\nPercentage Decay")
print(decay.round(2))



daily = df.groupby("InvoiceDate")["Revenue"].sum()

rolling30 = daily.rolling(30, min_periods=1).sum()

cum_spend = np.cumsum(rolling30)

print("\nRolling Spend")
print(rolling30)

print("\nCumulative Spend")
print(cum_spend)


fig, ax = plt.subplots(figsize=(10,6))

heat = ax.imshow(
    retention.fillna(0),
    cmap="YlGnBu",
    aspect="auto"
)

ax.set_xticks(range(len(retention.columns)))
ax.set_xticklabels(retention.columns)

ax.set_yticks(range(len(retention.index)))
ax.set_yticklabels(retention.index.astype(str))

plt.xlabel("Months Since First Purchase")
plt.ylabel("Cohort Month")
plt.title("Customer Cohort Retention (%)")

for i in range(retention.shape[0]):
    for j in range(retention.shape[1]):
        value = retention.iloc[i,j]
        if not np.isnan(value):
            ax.text(
                j,
                i,
                f"{value:.0f}%",
                ha="center",
                va="center",
                color="black"
            )

plt.colorbar(heat)
plt.tight_layout()
plt.show()