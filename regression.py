import pandas as pd
import quandl
import math

# df = data frame
df = quandl.get('WIKI/GOOGL')
df = df[['Adj. Open','Adj. High', 'Adj. Low', 'Adj. Close' ,'Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Low'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

forecast_col = 'Adj. Close'

# in PANDAS, .fillna() fills NaNs with designated argument
# PROTIP - Don't wanna get rid of data in Machine Learning,
# Instead force it to be a outlier (-9999)
df.fillna(-99999, inplace=True)

# Using a weeks data to determine forecast price today
# Predict out 10% of the data frame
forecast_out = int(math.ceil(0.01 * len(df)))

#shifting the columns negatively
df['label'] = df[forecast_col].shift(-forecast_out)

#prints first five rows of the dataframe
print(df.head())
