import pandas as pd

product_data = pd.read_excel("input.xlsx")

product_data["Total"] = product_data["Price"] * product_data["Quantity"]
print(product_data)

product_data.to_excel("output.xlsx", index=False)