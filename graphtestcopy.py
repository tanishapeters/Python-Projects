# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 12:27:09 2020

@author: tanis
"""
import pandas as pd
import pandas_datareader as pdr
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib.pyplot import style
#from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
 #                              AutoMinorLocator)
import matplotlib.ticker as mticker
import psycopg2 as pg2
import sqlalchemy 
import matplotlib.animation as animation
#from matplotlib.finance import candlestick_ohlc

style.use ("ggplot")
engine= sqlalchemy.create_engine('postgresql://postgres:SimplePW1@localhost:5432/GASCI')
#df=pd.read_sql_table("dihtradedata", engine, parse_dates=True, index_col=0)
# df=pd.read_sql_table("dihtradedata", engine, parse_dates=True, 
# columns=('issuer_id','ticker',
#          'trade_date','opening_price',
#          'low', 'high','last_trade_price',
#          'volume_traded'), index_col=0)


#df=pd.read_sql_table("dihtradedata", engine)

# query ='''SELECT trade_date, low, high FROM dihtradedata 
# WHERE trade_date BETWEEN '2019-04-01' AND '2019-04-30' '''
# df=pd.read_sql_query(query, engine)


# query ='''SELECT trade_date, low, high
# FROM dihtradedata 
# WHERE DATE_TRUNC('MONTH', trade_date) = DATE_TRUNC('MONTH',CURRENT_DATE);
#   '''
  
query ='''Select trade_date, low, high FROM dihtradedata
WHERE trade_date>CURRENT_DATE - interval '31' day;;
  ''' 
#Looks for the last 31 days of data from the current date

df=pd.read_sql_query(query, engine)
df.set_index(['trade_date'], inplace=True)

#df.xaxis.set_minor_locator(MultipleLocator(6))
#ax=plt.xticks(6)

#df=df.astype({"low":'float',"trade_date":'O',}) #matplotlib cannot plot the date time format so it is converted to an object

df[['low','high']].plot()
#plt.xscale(10)
plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(6))#c

#plt.xticks([5])
# ax=plt.gca()
# ax.set_xticks.set_minor_locator(MultipleLocator(6))
# print (ax)
plt.show()
#
##df[:10].plot()
#plt.show()
print(df.head(10))
#print(df[['high', 'trade_date']])

#link='/Users/tanis/stockTradesT.csv'
#style.use ("ggplot")
#df=pd.read_csv(link, parse_dates=True, index_col=0) #Or stockTradesT.csv
#print(df.head)
#df.plot('ticker', 'High')
##df.plot()
#plt.show()


#....


#start=dt.datetime(2010,1,4)
#end=dt.datetime (2010,1,6)


#df.plot() #plots the entire thing
#print(df[['low','high']].head())


