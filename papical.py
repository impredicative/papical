import sys

import pandas as pd

df_path = sys.argv[1]  # if sys.argv[1:] else SAMPLE_PATH
df = pd.read_csv(df_path,
                usecols=['Order Date', 'Order ID', 'ASIN/ISBN', 'Condition', 'Quantity', 'Item Total'],
                parse_dates=['Order Date'],
                converters={'Item Total': lambda s: float(s.lstrip('$').replace(',', ''))},
                )
df.rename(columns={'Order Date': 'Date', 'Order ID': 'Order', 'ASIN/ISBN': 'Product', 'Item Total': 'Cost'}, inplace=True)
df = df[df['Condition']=='new']
del df['Condition']
df = df[(df['Quantity'] >= 1) & (df['Cost'] > 0)]
assert df['Date'].is_monotonic_increasing
assert (df['Product'].notna() & (df['Product'] != "")).all()
df.drop_duplicates(subset=['Order', 'Product'], inplace=True)
del df['Order']
df.reset_index(drop=True, inplace=True)

df_date_ranges = df['Date'].drop_duplicates()[::-1].reset_index(drop=True).to_frame(name='LaterEnd')
df_date_ranges['LaterBegin'] = df_date_ranges['LaterEnd'] - pd.DateOffset(years=1, days=-1)
df_date_ranges['BaseEnd'] = df_date_ranges['LaterBegin'] - pd.DateOffset(days=1)
df_date_ranges['BaseBegin'] = df_date_ranges['BaseEnd'] - pd.DateOffset(years=1, days=-1)
oldest_order_date = df['Date'].min()
df_date_ranges = df_date_ranges[df_date_ranges['BaseBegin'] >= oldest_order_date]

# inflation = []
for date_range in df_date_ranges.itertuples():
    df_later = df[(date_range.LaterBegin <= df['Date']) & (df['Date'] <= date_range.LaterEnd)]
    df_base = df[(date_range.BaseBegin <= df['Date']) & (df['Date'] <= date_range.BaseEnd)]
    df_later = df_later[['Product', 'Quantity', 'Cost']]
    df_base = df_base[['Product', 'Quantity', 'Cost']]
    common_products = pd.merge(df_later['Product'], df_base['Product'], how='inner')['Product'].drop_duplicates()
    if common_products.empty:
        continue
    df_later = df_later[df_later['Product'].isin(common_products)].groupby('Product').sum()
    df_base = df_base[df_base['Product'].isin(common_products)].groupby('Product').sum()
    df_later['AvgCost'] = df_later['Cost'] / df_later['Quantity']
    df_base['AvgCost'] = df_base['Cost'] / df_base['Quantity']
    del df_later['Cost'], df_base['Cost']
    df_date_range = pd.merge(df_later, df_base, on='Product', suffixes=('Later', 'Base'), validate='1:1')
    df_date_range['LaspeyresCostLater'] = df_date_range['AvgCostLater'] * df_date_range['QuantityBase']
    df_date_range['LaspeyresCostBase'] = df_date_range['AvgCostBase'] * df_date_range['QuantityBase']
    df_date_range['PaascheCostLater'] = df_date_range['AvgCostLater'] * df_date_range['QuantityLater']
    df_date_range['PaascheCostBase'] = df_date_range['AvgCostBase'] * df_date_range['QuantityLater']
    df_date_range = df_date_range[['LaspeyresCostLater', 'LaspeyresCostBase', 'PaascheCostLater', 'PaascheCostBase']]
    num_items = len(df_date_range)
    cost_sums = df_date_range.sum()
    laspeyres = (cost_sums['LaspeyresCostLater'] / cost_sums['LaspeyresCostBase']) - 1
    paasche = (cost_sums['PaascheCostLater'] / cost_sums['PaascheCostBase']) - 1
    later_end_date = date_range.LaterEnd.date()
    # inflation.append({'Date': later_end_date, 'NumItems': num_items, 'Laspeyres': laspeyres, 'Paasche': paasche})
    print(f'[LastOrderDate={later_end_date}] NumCommonUniqueItems={num_items:,}, Laspeyres={laspeyres:.1%}, Paasche={paasche:.1%}')
# df_inflation = pd.DataFrame(inflation)
# print(df_inflation)