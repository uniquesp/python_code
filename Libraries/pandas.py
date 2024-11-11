import pandas as pd

# 1. Creating DataFrames and Series
# ---------------------------------
print("1. Creating DataFrames and Series")

# Creating a Series
s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print("Series:\n", s)

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
    'Salary': [70000, 80000, 120000, 110000]
}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)


# 2. Basic Operations
# -------------------
print("\n2. Basic Operations")

# Displaying basic information
print("Data types:\n", df.dtypes)
print("Shape:", df.shape)
print("Column names:", df.columns)
print("First two rows:\n", df.head(2))
print("Last two rows:\n", df.tail(2))

# Describe statistics for numeric columns
print("\nDescriptive statistics:\n", df.describe())

# Selecting a column (returns a Series)
print("\nSelecting 'Age' column:\n", df['Age'])

# Selecting multiple columns (returns a DataFrame)
print("\nSelecting 'Name' and 'City' columns:\n", df[['Name', 'City']])

# Adding a new column
df['Bonus'] = [5000, 6000, 7000, 8000]
print("\nDataFrame with 'Bonus' column:\n", df)

# Removing a column
df = df.drop(columns=['Bonus'])
print("\nDataFrame after dropping 'Bonus' column:\n", df)


# 3. Indexing and Filtering
# -------------------------
print("\n3. Indexing and Filtering")

# Setting a new index
df = df.set_index('Name')
print("\nDataFrame with 'Name' as index:\n", df)

# Resetting index
df = df.reset_index()
print("\nDataFrame after resetting index:\n", df)

# Filtering rows
filtered_df = df[df['Age'] > 30]
print("\nRows where Age > 30:\n", filtered_df)

# Conditional selection with multiple conditions
multi_cond_df = df[(df['Age'] > 25) & (df['City'] == 'New York')]
print("\nRows where Age > 25 and City is New York:\n", multi_cond_df)


# 4. Grouping and Aggregation
# ---------------------------
print("\n4. Grouping and Aggregation")

# Creating a new DataFrame for demonstration
group_data = {
    'Department': ['HR', 'Finance', 'HR', 'Finance', 'IT', 'IT'],
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Salary': [60000, 70000, 80000, 90000, 50000, 60000]
}
df_group = pd.DataFrame(group_data)

# Group by and aggregate
grouped_df = df_group.groupby('Department').mean()
print("\nAverage Salary by Department:\n", grouped_df)

# Multiple aggregations
agg_df = df_group.groupby('Department').agg({'Salary': ['mean', 'sum']})
print("\nMean and Sum of Salary by Department:\n", agg_df)


# 5. Merging and Joining
# ----------------------
print("\n5. Merging and Joining")

# Creating DataFrames for merging
left = pd.DataFrame({
    'Employee': ['Alice', 'Bob', 'Charlie'],
    'Department': ['HR', 'Finance', 'IT']
})
right = pd.DataFrame({
    'Employee': ['Alice', 'Bob', 'Charlie'],
    'Salary': [60000, 70000, 80000]
})

# Merge on Employee column
merged_df = pd.merge(left, right, on='Employee')
print("\nMerged DataFrame:\n", merged_df)


# 6. Handling Missing Values
# --------------------------
print("\n6. Handling Missing Values")

# Creating DataFrame with missing values
data_with_na = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, None, 35, 40],
    'Salary': [70000, 80000, None, 110000]
}
df_na = pd.DataFrame(data_with_na)

# Detecting missing values
print("\nDataFrame with missing values:\n", df_na)
print("Is null:\n", df_na.isnull())

# Filling missing values
df_filled = df_na.fillna({'Age': df_na['Age'].mean(), 'Salary': 50000})
print("\nDataFrame after filling missing values:\n", df_filled)

# Dropping rows with missing values
df_dropped = df_na.dropna()
print("\nDataFrame after dropping rows with missing values:\n", df_dropped)


# 7. Sorting and Ranking
# ----------------------
print("\n7. Sorting and Ranking")

# Sorting by Age column
sorted_df = df.sort_values(by='Age', ascending=False)
print("\nDataFrame sorted by Age:\n", sorted_df)

# Sorting by multiple columns
sorted_multi_df = df.sort_values(by=['Age', 'Salary'], ascending=[True, False])
print("\nDataFrame sorted by Age and Salary:\n", sorted_multi_df)


# 8. Applying Functions
# ---------------------
print("\n8. Applying Functions")

# Using apply() to modify columns
df['Age'] = df['Age'].apply(lambda x: x + 1)
print("\nDataFrame after incrementing Age by 1:\n", df)

# Using apply() on multiple columns
df['Salary'] = df.apply(lambda row: row['Salary'] * 1.05 if row['City'] == 'New York' else row['Salary'], axis=1)
print("\nDataFrame after applying conditional increase to Salary:\n", df)


# 9. Pivot Tables
# ---------------
print("\n9. Pivot Tables")

pivot_df = pd.pivot_table(df_group, values='Salary', index='Department', aggfunc='mean')
print("\nPivot table of average salary by department:\n", pivot_df)


# 10. Date and Time Handling
# --------------------------
print("\n10. Date and Time Handling")

# Creating a date range
date_range = pd.date_range(start='2023-01-01', end='2023-01-10')
print("Date Range:\n", date_range)

# Creating DataFrame with dates
time_data = {
    'Date': pd.date_range(start='2023-01-01', periods=10, freq='D'),
    'Value': range(10)
}
df_time = pd.DataFrame(time_data)

# Set date as index
df_time.set_index('Date', inplace=True)
print("\nDataFrame with Date index:\n", df_time)

# Filtering by date
print("\nFilter by date:\n", df_time['2023-01-03':'2023-01-06'])

# Resampling time series data
print("\nResampled by 3 days (mean):\n", df_time.resample('3D').mean())
