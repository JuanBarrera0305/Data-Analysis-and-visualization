import pandas as pd

file_path = "BMW_Car_Sales_Classification.csv"
df = pd.read_csv(file_path)

df.columns = df.columns.str.strip()

print("===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== DATA INFO =====")
print(df.info())

print("\n===== BASIC STATS =====")
print(df.describe())


print("\n===== SEARCH 1: Cars from year 2020 =====")
print(df[df['Year'] == 2020])

print("\n===== SEARCH 2: Cars with Price above $50,000 =====")
print(df[df['Price_USD'] > 50000])


print("\n===== SEARCH 3: Cars with model name containing 'X5' =====")
print(df[df['Model'].str.contains("X5", case=False, na=False)])

print("\n===== SEARCH 4: Cars sold in a specific region (example: 'Europe') =====")
print(df[df['Region'].str.contains("Europe", case=False, na=False)])


print("\n===== SEARCH 5: Cars with Mileage less than 20,000 =====")
print(df[df['Mileage_KM'] < 20000])


filtered = df[df['Price_USD'] > 70000]
filtered.to_csv("High_Price_BMWs.csv", index=False)
print("\n Saved cars priced above $70,000 to High_Price_BMWs.csv")
