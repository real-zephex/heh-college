# Pandas Module

## Data Structures
Pandas has two primary data structures:
1. **Series**: A one-dimensional labeled array, similar to a list or a column in Excel.
2. **DataFrame**: A two-dimensional labeled data structure, like a table with rows and columns.

## Creating a Series
```python
data = pd.Series([10, 20, 30, 40, 34.3])
print(data)  # Prints the series along with the dtype of the elements
```

## Creating a DataFrame
```python
data = [
  ["Sumit", 18, ["Programming", "Sleeping"]],
  ["Sung Jin Woo", 18, ["Leveling up", "Saving the world"]],
  ["Sam", 16, ["Basketball", "Handicrafts"]]
]
df = pd.DataFrame(data, columns=["Name", "Age", "Hobbies"], index=[i+1 for i in range(len(data))])
print(df)  # Organizes data into rows and columns
```

## In-built Functions
- `df.head()`: Prints the top 5 rows.
- `df.tail()`: Prints the last 5 rows.
- `df.info()`: Provides a summary of the DataFrame.
- `df.describe()`: Provides statistics for numerical columns.

## Shapes and Columns
- `df.shape`: Returns the shape of the DataFrame.
- `df.columns`: Returns the column names.

## Indexing a DataFrame
```python
print(list(df.iloc[1]))  # Accesses the second row
print(df.iloc[0:1, 0:3])  # Accesses a subset of the DataFrame
```

## Data Filtering and Sorting
```python
filtered = df[df["Age"] < 18]
print(filtered)  # Filters rows where Age is less than 18

sorted_filtered = df.sort_values(by="Name", ascending=True)
print(sorted_filtered)  # Sorts the DataFrame by Name in ascending order
```

## Adding and Dropping Columns
```python
df['Salary'] = [50000, 60000, 70000]
print(df)  # Adds a new column 'Salary'

df = df.drop('Salary', axis=1)
print(df)  # Drops the 'Salary' column
```

## Handling Missing Data
```python
df.fillna(0, inplace=True)  # Replaces NaN with 0
df.dropna(inplace=False)  # Drops rows with NaN values
print(df)
```

## Aggregation and Grouping
```python
print(df["Age"].sum())  # Sums the 'Age' column
print(df["Age"].mean())  # Calculates the mean of the 'Age' column

grouped = df.groupby("Name")["Age"].sum()
print(grouped)  # Groups by 'Name' and sums the 'Age' column
```

## Reading CSV Files
```python
new_df = pd.read_csv("random_data.csv")
print(new_df.head())  # Prints the top 5 rows of the CSV file
print(new_df.tail())  # Prints the last 5 rows of the CSV file

print(new_df.sort_values(by="Salary", ascending=False))  # Sorts by 'Salary' in descending order
print(new_df["Salary"].sum())  # Sums the 'Salary' column
print(new_df["Salary"].mean())  # Calculates the mean of the 'Salary' column
```