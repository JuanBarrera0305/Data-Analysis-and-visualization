import pandas as pd
import matplotlib.pyplot as plt

# ================================
# STEP 1: Load the Dataset
# ================================
file_path = "movies_dataset.csv"  # <-- Your CSV file
df = pd.read_csv(file_path)

# ================================
# STEP 2: Review and Analyze Data
# ================================
print("===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== DATA TYPES =====")
print(df.dtypes)

print("\n===== SELECTED COLUMN: Genre =====")
print(df['Genre'])

print("\n===== MOVIES WITH IMDb RATING ABOVE 7.5 =====")
print(df[df['IMDb Rating'] > 7.5])

print("\n===== SORTED BY IMDb RATING (DESCENDING) =====")
print(df.sort_values(by='IMDb Rating', ascending=False))

# ================================
# STEP 3: Visualizations
# ================================

# 1. Bar Chart – Box Office Earnings by Movie
plt.figure(figsize=(10, 6))
plt.bar(df['Movie Title'], df['Box Office Earnings ($M)'], color='skyblue')
plt.xticks(rotation=45, ha='right')
plt.title('Box Office Earnings by Movie')
plt.xlabel('Movie Title')
plt.ylabel('Earnings ($M)')
plt.tight_layout()
plt.savefig('barchart.png')
plt.close()

# 2. Pie Chart – Genre Distribution
genre_counts = df['Genre'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(genre_counts, labels=genre_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Genre Distribution')
plt.tight_layout()
plt.savefig('piechart.png')
plt.close()

# 3. Scatter Plot – IMDb Rating vs Box Office Earnings
plt.figure(figsize=(8, 6))
plt.scatter(df['IMDb Rating'], df['Box Office Earnings ($M)'], color='green')
plt.title('IMDb Rating vs Box Office Earnings')
plt.xlabel('IMDb Rating')
plt.ylabel('Box Office Earnings ($M)')
plt.grid(True)
plt.tight_layout()
plt.savefig('scatterplot.png')
plt.close()

# 4. Line Chart – Total Box Office Earnings by Year
yearly_earnings = df.groupby('Release Year')['Box Office Earnings ($M)'].sum()
plt.figure(figsize=(8, 6))
plt.plot(yearly_earnings.index, yearly_earnings.values, marker='o', color='purple')
plt.title('Total Box Office Earnings by Year')
plt.xlabel('Release Year')
plt.ylabel('Total Earnings ($M)')
plt.grid(True)
plt.tight_layout()
plt.savefig('linegraph.png')
plt.close()

# ================================
# STEP 4: Export DataFrame to CSV
# ================================
df.to_csv('movies_dataset_updated.csv', index=False)

print("\n✅ Analysis complete. Charts and updated CSV have been saved successfully.")
