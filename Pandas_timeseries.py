import pandas as pd
df = pd.read_csv('data/ETH_1H.csv')  # no parsing od dates.
#df = pd.read_csv('data/ETH_1H.csv', parse_dates=['Date'], date_parser=d_parser)  # parsing dates while reading the csv file. This is more efficient than parsing the dates after reading the csv file.
print(df.head())
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %I-%p') # not required if we have already parsed the dates while reading the csv file. This is just to show how to parse the dates after reading the csv file.
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior   - for more details on the format codes used in the above line of code.
# print(df.dtypes)
print("***************************************")
print(df.loc[0,'Date'].day_name())  # to get the day name from the date column.
df['DayOfWeek'] = df['Date'].dt.day_name()  # to create a new column with the day name.
print(df['Date'].dt.month_name())  # to get the month name from the date column.
print(df['Date'].min()) # to get the minimum date in the date column.
print(df['Date'].max()) # to get the maximum date in the date column.
print(df['Date'].max() - df['Date'].min()) # to get the difference between the maximum and minimum date in the date column.

filt = (df['Date'] >= pd.to_datetime('2019-01-01')) & (df['Date'] < pd.to_datetime('2020-01-01'))  
print(df.loc[filt])  # to filter the dataframe based on the date column.


df.set_index('Date', inplace=True)  # to set the date column as the index of the dataframe.
df.sort_index(inplace=True)  # to sort the dataframe based on the date index. This is important for resampling the dataframe later on.
print(df.head())
print(df['2020-01-01':'2020-02-29']['Close'].mean())

# to filter/slice the dataframe based on the date index. This will return all the rows between January 2020 and March 2020 (inclusive).


#  https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#dateoffset-objects   -  Pandas Date Offset Codes

Daily_highs = df['High'].resample('D').max()  # to resample the dataframe to daily frequency and get the maximum value of the 'High' column for each day.
print(Daily_highs['2020-01-01'])

Weekly_candle = df.resample('W').agg({'Open':'first', 'High':'max', 'Low':'min', 'Close':'last', 'Volume':'sum'})  # to resample the dataframe to weekly frequency and get the first value of the 'Open' column, maximum value of the 'High' column, minimum value of the 'Low' column, last value of the 'Close' column and sum of the 'Volume' column for each week.
print(Weekly_candle.head(10))

# ------------- works in Jupyter Notebook only -------------
# %matplotlib inline
# Daily_highs.plot()  # to plot the daily highs. This will give us a line plot of the daily highs.



