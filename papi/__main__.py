import sys

import pandas as pd

DF_PATH = sys.argv[1]
INPUT_USED_COLS = ['Order Date', 'Title', 'ASIN/ISBN', 'Condition', 'Quantity', 'Item Total']

df = pd.read_csv(DF_PATH, usecols=INPUT_USED_COLS, parse_dates=['Order Date'])
df.rename(columns={'Order Date': 'Date', 'ASIN/ISBN': 'ASIN', 'Item Total': 'TotalCost'}, inplace=True)
df = df[df['Condition']=='new']
del df['Condition']
assert df['ASIN'].notna().all()
assert not (df['ASIN'] == "").any()
print(df)
print(df.dtypes)
