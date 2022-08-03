import sys

import pandas as pd

DF_PATH = sys.argv[1]
df = pd.read_csv(DF_PATH)
print(df)
print(df.dtypes)
