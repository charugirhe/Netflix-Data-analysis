# Netflix Dataset Analysis
# Description: Data cleaning, exploration, and visualization of Netflix titles dataset

import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('netflix_titles.csv')

# Print basic info
print("First 5 rows of dataset:\n", df.head())
print("\nShape of dataset:", df.shape)
print("\nMissing values in each column:\n", df.isnull().sum())
print("\nColumn names:\n", df.columns)

# Handling missing values

# Fill missing with 'unknown' for some columns
df['director'] = df['director'].fillna('unknown')
df['cast'] = df['cast'].fillna('unknown')
df['country'] = df['country'].fillna('unknown')
df['rating'] = df['rating'].fillna('unknown')

# Drop rows where 'date_added' or 'duration' is missing
df = df.dropna(subset=['date_added', 'duration'])

# Confirm changes
print("\nMissing values after cleaning:\n", df.isnull().sum())
print("Shape after cleaning:", df.shape)

# Value counts for exploration
print("\nType count (Movie vs TV Show):\n", df['type'].value_counts())
print("\nTop Genres:\n", df['listed_in'].value_counts().head())
print("\nTop Countries:\n", df['country'].value_counts().head())
print("\nRating distribution:\n", df['rating'].value_counts())
print("\nTop Directors:\n", df['director'].value_counts().head())
print("\nDuration types:\n", df['duration'].value_counts().head())

# Handle 'date_added' column
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')  # invalid = NaT
df['year'] = df['date_added'].dt.year  # extract year from date

# Print sample date info
print("\nTitle with Year of Addition:\n", df[['title', 'date_added', 'year']].head())

# Grouping and sorting
print("\nContent count by year:\n", df.groupby('year')['title'].count())
print("\nOldest content:\n", df.sort_values('year').head())


# Visualizations

# 1. Movie vs TV Show Count
plt.figure(figsize=(10,6))
sns.countplot(x='type', data=df,hue='type', palette='pastel')
plt.title("Count of Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()

# 2. Rating distribution
plt.figure(figsize=(12,6))
sns.countplot(x='rating', data=df,hue='type', palette='Set2')
plt.title("Distribution of Content Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# 3. Content by Year and Type
plt.figure(figsize=(14,6))
sns.countplot(x='year', data=df, hue='type', palette='coolwarm')
plt.title("Content Added Each Year (Movies vs TV Shows)")
plt.xlabel("Year")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# 4. Top 10 Countries with Most Content
plt.figure(figsize=(12,6))
df['country'].value_counts().head(10).plot(kind='bar', color='lightseagreen')
plt.title("Top 10 Countries by Number of Titles")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.show()

# 5. Top 10 Genres
plt.figure(figsize=(12,6))
df['listed_in'].value_counts().head(10).plot(kind='bar', color='mediumorchid')
plt.title("Top 10 Genres")
plt.xlabel("Genre")
plt.ylabel("Number of Titles")
plt.show()

# 6. Pie Chart - Movie vs TV Show
plt.figure(figsize=(8,8))
df['type'].value_counts().plot(kind='pie',  autopct='%1.1f%%', startangle=90, colors=['lightcoral', 'skyblue'])
plt.title("Movie vs TV Show - Percentage")
plt.ylabel("")  # removes y-axis label
plt.show()
