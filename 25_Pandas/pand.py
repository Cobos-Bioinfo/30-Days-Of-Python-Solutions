# Day 25 - 30DaysOfPython Challenge
# Pandas

import pandas as pd

# 1 - Read the hacker_news.csv file from data directory
df = pd.read_csv("./data/hacker_news.csv")

# 2 - Get the first five rows
print(f"\n=== First 5 rows: ===\n{df.head()}\n")

# 3 - Get the last five rows
print(f"\n=== Last 5 rows: ===\n{df.tail()}\n")

# 4 - Get the title column as pandas series
title_col = df["title"]
print(f"\n=== Title column as pandas series: ===\n{title_col.head()}\n")

# 5 - Count the number of rows and columns
print(f"\n=== Shape (rows, columns): ===\n{df.shape}\n")

    # Filter the titles which contain python
python_titles = df[title_col.str.contains("python", case=False, na=False)]
print(f"\n=== Titles containing 'Python': ===\n"
      f"{python_titles["title"].to_string(index=False)}\n"
      )
    

    # Filter the titles which contain JavaScript
js_titles = df[title_col.str.contains("javascript", case=False, na=False)]
print(f"\n=== Titles containing 'JavaScript': ===\n"
      f"{js_titles["title"].to_string(index=False)}\n"
      )

    # Explore the data and make sense of it
print("=== Data Exploration ===")
print("\nColumn names:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nTop authors by number of posts:")
print(df["author"].value_counts().head())

print("\nAverage number of comments per post:")
print(df["num_comments"].mean())

print("\nMost upvoted story:")
# df["num_points"] selects the num_points column
# id.max() returns the index (row label) where num_points has max value
# df.loc[] selects the entire row by index label
# [["title", "num_points", "author"]] from that row select only these 3 columns.
print(df.loc[df["num_points"].idxmax()][["title", "num_points", "author"]])
