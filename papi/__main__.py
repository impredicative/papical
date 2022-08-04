import sys

import pandas as pd

DF_PATH = sys.argv[1]
INPUT_USED_COLS = ['Order Date', 'Order ID', 'Title', 'ASIN/ISBN', 'Condition', 'Quantity', 'Item Total']

df = pd.read_csv(DF_PATH, usecols=INPUT_USED_COLS, parse_dates=['Order Date'],
                converters={'Item Total': lambda s: float(s.lstrip('$').replace(',', ''))},
                )
df.rename(columns={'Order Date': 'Date', 'Order ID': 'Order', 'ASIN/ISBN': 'ASIN', 'Item Total': 'TotalCost'}, inplace=True)
df = df[df['Condition']=='new']
del df['Condition']
df = df[(df['Quantity'] >= 1) & (df['TotalCost'] > 0)]
assert df['Date'].is_monotonic_increasing
assert (df['ASIN'].notna() & (df['ASIN'] != "")).all()
df.drop_duplicates(subset=['Order', 'ASIN'], inplace=True)
del df['Order']
print(df)
print(df.dtypes)
