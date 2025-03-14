import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_excel("DATA.xlsx", sheet_name=0, index_col=0, parse_dates=True)
data_returns = data.get('RETURNS')
data_PB = data.get('PRICE TO BOOK')
data_benchmark = data.get('BENCHMARK RETURNS')

print(data.columns)
print(data.head())



#def momentum_score(df_returns):
