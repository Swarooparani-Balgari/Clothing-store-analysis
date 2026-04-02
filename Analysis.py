import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_excel("TASK 9.xlsx",sheet_name="Dataset")

df["DiscountAmount"]=df["Price"]*df["DiscountPercent"]/100
df["FinalPrice"]=df["Price"]*df["DiscountAmount"]
df["Revenue"]=df["Quantity"]*df["FinalPrice"]

## Total Revenue
print("Total_Revenue:",df["Revenue"].sum())

## Revenue by Category
print("\nRevenue by Category\n",df.groupby("Category")["Revenue"].sum().sort_values(ascending=False))

## Revenue by City
print("\nRevenue by Product\n",df.groupby("Product")["Revenue"].sum().sort_values(ascending=False))

## Discount analysis
print("\nDiscount Analysis\n",df.groupby("DiscountPercent")["Quantity"].sum().sort_values(ascending=False))

## Visualizations

df.groupby("City")["Revenue"].sum().sort_values(ascending=True).plot(kind="bar")
plt.title("Revenue by City")
plt.show()

df.groupby("Product")["Quantity"].sum().sort_values(ascending=False).plot(kind="pie")
plt.title("Product by Quantity")
plt.show()


