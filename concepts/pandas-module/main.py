# Pandas Module
import pandas as pd

# Data Structures
"""
Pandas has 2 data structures
  1. Series
  2. Dataframe

Series is a one dimensional labeled array, similar to a list or a column in excel.

Dataframe is a two dimensional labeled data structure, like a table with rows and columns
"""

data = pd.Series([10, 20, 30, 40, 34.3])
print(data) # printing a series wll also print the dtype of the elements

data = [
  ["Sumit", 18, ["Programming", "Sleeping"]],
  ["Sung Jin Woo", 18, ["Leveling up", "Saving the world"]],
  ["Sam", 16, ["Basketball", "Handicrafts"]]
]
df = pd.DataFrame(data, columns=["Name", "Age", "Hobbies"], index=[i+1 for i in range(len(data))])
print(df) # Printing the dataframe will organize the data into rows and columns where the keys are the column names and the row numbers are automaitcally assigned starting from 0.

# In-built functions
print(df.head()) # Prints the top 5 rows 
print(df.tail()) # Prints the last 5 rows
print(df.info()) # Summary of the dataframe
print(df.describe()) # Statistics for numerical columns

# Shapes and columns
print(df.shape)
print(df.columns)

# Indexing a pandas dataframe
print(list(df.iloc[1])) 

print(df.iloc[0:1, 0:3])

print()

# Data filtering and sorting
filtered = df[df["Age"] < 18]
print(filtered)

sorted_filtered = df.sort_values(by="Name", ascending=True)
print(sorted_filtered)

# Adding and dropping column
df['Salary'] = [50000, 60000, 70000]
print(df)

df = df.drop('Salary', axis=1)  # axis=1 means column
print(df)

df.fillna(0, inplace=True) # Repalce NaN with 0
df.dropna(inplace=False) # Drop rows with NaN values
print(df)

# Aggregation and Grouping
print(df["Age"].sum())
print(df["Age"].mean())

grouped = df.groupby("Name")["Age"].sum()
print(grouped)

# Reading CSV files using pandas
new_df = pd.read_csv("random_data.csv")
print(new_df.head())
print(new_df.tail())
print()
print(new_df.sort_values(by="Salary", ascending=False))
print(new_df["Salary"].sum())
print(new_df["Salary"].mean())
