import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import zscore

# Load data
file_path = "DATA.xlsx"

df_returns = pd.read_excel(file_path, sheet_name="RETURNS", index_col=0).dropna()
df_PB = pd.read_excel(file_path, sheet_name="PRICE TO BOOK", index_col=0).dropna()
df_benchmark = pd.read_excel(file_path, sheet_name="BENCHMARK RETURNS", index_col=0).dropna()

# print(df_returns.head())
# print(df_PB.head())
# print(df_benchmark.head())


def calculate_momentum_scores(df_returns):
    mean_returns = df_returns.rolling(window=12, min_periods=12).mean()
    std_returns = df_returns.rolling(window=12, min_periods=12).std()
    momentum_scores = (df_returns - mean_returns) / std_returns
    # momentum_scores = momentum_scores.dropna()
    return momentum_scores.apply(zscore, axis=1)


def calculate_pb_scores(df_PB):
    pb_score = 1 / df_PB.shift(1)
    # pb_score = pb_score.dropna()
    return pb_score.apply(zscore, axis=1)

print("\n\n")
momentum_scores = calculate_momentum_scores(df_returns)
print('\nMomentum Scores:\n', momentum_scores.head())
print(momentum_scores.tail())
pb_scores = calculate_pb_scores(df_PB)
print('\nPB Scores:\n', pb_scores.head())
print(pb_scores.tail())

global_scores = (momentum_scores + pb_scores) / 2
global_scores = global_scores.dropna()
print('\nGlobal Scores:\n', global_scores.head())


def portfolio_construction(global_scores):
    long_portfolio = global_scores[global_scores > 0].mean(axis=1)
    short_portfolio = global_scores[global_scores < 0].mean(axis=1)
    return long_portfolio, short_portfolio

long_portfolio, short_portfolio = portfolio_construction(global_scores)
print('\nLong Portfolio:\n', long_portfolio.head())
print('\nShort Portfolio:\n', short_portfolio.head())



