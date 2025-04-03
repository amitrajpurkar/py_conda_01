import pandas as pd

df = pd.read_csv('Duval_StJohns.csv')
print(df.head(10))

df_info = df.describe()
print(df_info)

# df = pd.read_csv('Duval_StJohns.csv', index_col='Date')
# print(df.head(10))