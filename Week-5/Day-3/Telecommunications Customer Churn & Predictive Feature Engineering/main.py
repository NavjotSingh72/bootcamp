import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("telecom_churn.csv")

df = pd.get_dummies(df, columns=["Gender", "ContractType"])


df["TenureGroup"] = pd.qcut(df["Tenure"], q=3,
                            labels=["Low","Medium","High"])

Q1 = np.percentile(df["MonthlyCharges"],25)
Q3 = np.percentile(df["MonthlyCharges"],75)

IQR = Q3 - Q1

Lower = Q1 - 1.5*IQR
Upper = Q3 + 1.5*IQR

Outliers = df[(df["MonthlyCharges"] < Lower) |
             (df["MonthlyCharges"] > Upper)]

print("Outliers")
print(Outliers)


print(df)

plt.figure(figsize=(10,8))

plt.subplot(2,2,1)
plt.hist(df["MonthlyCharges"])
plt.title("Monthly Charges")

plt.subplot(2,2,2)
plt.boxplot(df["MonthlyCharges"])
plt.title("Monthly Charges Boxplot")

plt.subplot(2,2,3)
plt.hist(df["Tenure"])
plt.title("Tenure")

plt.subplot(2,2,4)
plt.boxplot(df["Tenure"])
plt.title("Tenure Boxplot")

plt.tight_layout()
plt.show()