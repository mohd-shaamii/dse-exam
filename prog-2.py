import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [28, 35, 40, 25],
    'Salary': [5000, 6000, 8000, 4500]
}
df = pd.DataFrame(data)

print("First few rows")
print(df.head())

print("\n Summary statistics:")
print(df.describe())

filtered_data = df[df['Age'] > 30]
print("\n Filtered data(Age>30):")
print(filtered_data)

sorted_data = df.sort_values(by='Salary', ascending=False)
print("\nSorted data(by Salary):")
print(sorted_data)

df['Bonus'] = df['Salary'] * 0.1
print("\n Data with new column(Bonus)")
print(df)

df.to_excel('Output.xlsx', index=False)
print("\n Data written to output.xlsx")
