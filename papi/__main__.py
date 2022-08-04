import sys

import pandas as pd

SAMPLE_PATH = './sample.csv'
INPUT_USED_COLS = ['Order Date', 'Order ID', 'Title', 'ASIN/ISBN', 'Condition', 'Quantity', 'Item Total']

df_path = sys.argv[1] if sys.argv[1:] else SAMPLE_PATH
df = pd.read_csv(df_path, usecols=INPUT_USED_COLS, parse_dates=['Order Date'],
                converters={'Item Total': lambda s: float(s.lstrip('$').replace(',', ''))},
                )
df.rename(columns={'Order Date': 'Date', 'Order ID': 'Order', 'ASIN/ISBN': 'Product', 'Item Total': 'Total'}, inplace=True)
df = df[df['Condition']=='new']
del df['Condition']
df = df[(df['Quantity'] >= 1) & (df['Total'] > 0)]
assert df['Date'].is_monotonic_increasing
assert (df['Product'].notna() & (df['Product'] != "")).all()
df.drop_duplicates(subset=['Order', 'Product'], inplace=True)
del df['Order']
df.reset_index(drop=True, inplace=True)
# print(df)
# print(df.dtypes)

df_date_ranges = df['Date'].drop_duplicates()[::-1].reset_index(drop=True).to_frame(name='LaterEnd')
df_date_ranges['LaterBegin'] = df_date_ranges['LaterEnd'] - pd.DateOffset(years=1, days=-1)
df_date_ranges['BaseEnd'] = df_date_ranges['LaterBegin'] - pd.DateOffset(days=1)
df_date_ranges['BaseBegin'] = df_date_ranges['BaseEnd'] - pd.DateOffset(years=1, days=-1)
oldest_order_date = df['Date'].min()
df_date_ranges = df_date_ranges[df_date_ranges['BaseBegin'] >= oldest_order_date]
# print(df_date_ranges)

for date_range in df_date_ranges.itertuples():
    df_later = df[(date_range.LaterBegin <= df['Date']) & (df['Date'] <= date_range.LaterEnd)]
    df_base = df[(date_range.BaseBegin <= df['Date']) & (df['Date'] <= date_range.BaseEnd)]
    common_products = pd.merge(df_later['Product'], df_base['Product'], how='inner')['Product'].drop_duplicates()
    if len(common_products) == 0:
        continue
    df_later = df_later[df_later['Product'].isin(common_products)]
    df_base = df_base[df_base['Product'].isin(common_products)]
    