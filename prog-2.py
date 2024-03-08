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

# OUTPUT:

# First few rows
#       Name  Age  Salary
# 0    Alice   28    5000
# 1      Bob   35    6000
# 2  Charlie   40    8000
# 3    David   25    4500

#  Summary statistics:
#             Age       Salary
# count   4.00000     4.000000
# mean   32.00000  5875.000000
# std     6.78233  1547.847968
# min    25.00000  4500.000000
# 25%    27.25000  4875.000000
# 50%    31.50000  5500.000000
# 75%    36.25000  6500.000000
# max    40.00000  8000.000000

#  Filtered data(Age>30):
#       Name  Age  Salary
# 1      Bob   35    6000
# 2  Charlie   40    8000

# Sorted data(by Salary):
#       Name  Age  Salary
# 2  Charlie   40    8000
# 1      Bob   35    6000
# 0    Alice   28    5000
# 3    David   25    4500

#  Data with new column(Bonus)
#       Name  Age  Salary  Bonus
# 0    Alice   28    5000  500.0
# 1      Bob   35    6000  600.0
# 2  Charlie   40    8000  800.0
# 3    David   25    4500  450.0

#  Data written to output.xlsx
