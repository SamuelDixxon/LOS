# -*- coding: utf-8 -*-
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2000,1,1)
end = dt.datetime(2020,1,1)
##
df = web.DataReader('AAPL', 'yahoo', start, end)

df.to_csv('AAPL.csv')
df = pd.read_csv('AAPL.csv', parse_dates=True, index_col=0)

df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
df.dropna(inplace=True)

'''ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)

ax1.plot(df.index, df['Adj Close'], label='Adjusted Close')
ax1.plot(df.index, df['100ma'], label='100 moving average')
ax2.bar(df.index, df['Volume'])
plt.show'''

df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()
a = plt.plot(df_volume), plt.title("Volume vs. Time"), plt.xlabel("Time (years)", color="r"), plt.ylabel("Volume", color="r")

print(df_ohlc.head())



