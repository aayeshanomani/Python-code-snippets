import pandas as pd
df = pd.read_csv('Tech.csv')
print(df)
print(df.columns)
print(df.head())
for col in df.columns:
    if col[:2] == 'nu':
        df.rename(columns = { col: 'Employees'}, inplace = True)
print(df.head())