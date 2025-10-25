import pandas as pd
import matplotlib.pyplot as plt

# 🎬 Step 1: Create the movie dataset
movies_data = {
    'Movie Title': ['The Dark Knight', 'Inception', 'Titanic', 'Toy Story', 'The Matrix',
                    'Interstellar', 'Parasite', 'Gladiator', 'Pulp Fiction', 'Forrest Gump'],
    'Genre': ['Action', 'Sci-Fi', 'Romance', 'Animation', 'Sci-Fi',
              'Sci-Fi', 'Thriller', 'Action', 'Crime', 'Drama'],
    'Release Year': [2008, 2010, 1997, 1995, 1999, 2014, 2019, 2000, 1994, 1994],
    'IMDb Rating': [9.0, 8.8, 7.9, 8.3, 8.7, 8.6, 8.6, 8.5, 8.9, 8.8],
    'Box Office Earnings ($M)': [1004.6, 829.9, 2187.5, 373.6, 463.5, 677.5, 263.1, 460.5, 213.9, 678.2]
}

df = pd.DataFrame(movies_data)

# 🎯 Step 2: Bar Chart – Box Office Earnings by Movie
plt.figure(figsize=(10, 6))
plt.bar(df['Movie Title'], df['Box Office Earnings ($M)'], color='skyblue')
plt.xticks(rotation=45, ha='right')
plt.title('Box Office Earnings by Movie')
plt.xlabel('Movie Title')
plt.ylabel('Earnings ($M)')
plt.tight_layout()
plt.savefig('barchart.png')
plt.close()

# 🎯 Step 3: Pie Chart – Genre Distribution
genre_counts = df['Genre'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(genre_counts, labels=genre_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Genre Distribution')
plt.tight_layout()
plt.savefig('piechart.png')
plt.close()

# 🎯 Step 4: Scatter Plot – IMDb Rating vs Box Office Earnings
plt.figure(figsize=(8, 6))
plt.scatter(df['IMDb Rating'], df['Box Office Earnings ($M)'], color='green')
plt.title('IMDb Rating vs Box Office Earnings')
plt.xlabel('IMDb Rating')
plt.ylabel('Box Office Earnings ($M)')
plt.grid(True)
plt.tight_layout()
plt.savefig('scatterplot.png')
plt.close()

# 🎯 Step 5: Line Chart – Total Box Office Earnings by Year
yearly_earnings = df.groupby('Release Year')['Box Office Earnings ($M)'].sum()
plt.figure(figsize=(8, 6))
plt.plot(yearly_earnings.index, yearly_earnings.values, marker='o', color='purple')
plt.title('Total Box Office Earnings by Year')
plt.xlabel('Release Year')
plt.ylabel('Total Earnings ($M)')
plt.grid(True)
plt.tight_layout()
plt.savefig('linegarph.png')
plt.close()

# 📝 Optional: Save dataset to CSV
df.to_csv('movies_dataset.csv', index=False)
