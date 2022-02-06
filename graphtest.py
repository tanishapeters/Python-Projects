# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 12:27:09 2020

@author: tanis
"""
#%matplotlib inline
import pandas as pd
import pandas_datareader as pdr
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib.pyplot import style
import matplotlib.ticker as mticker
import psycopg2 as pg2
import sqlalchemy 
from matplotlib.animation import FuncAnimation
#from matplotlib.finance import candlestick_ohlc
import ipywidgets as widgets
from itertools import count
from pandas.plotting import register_matplotlib_converters


style.use ("ggplot")
engine= sqlalchemy.create_engine('postgresql://postgres:SimplePW1@localhost:5432/GASCI')

query ='''Select trade_date, low, high FROM dihtradedata
WHERE trade_date>CURRENT_DATE - interval '31' day;''' 
#Looks for the last 31 days of data from the current date

query2 ='''SELECT trade_date, low, high FROM dihtradedata 
WHERE trade_date BETWEEN '2019-04-01' AND '2019-04-30' '''
#df=pd.read_sql_query(query, engine)

# query ='''SELECT trade_date, low, high
# FROM dihtradedata 
# WHERE DATE_TRUNC('MONTH', trade_date) = DATE_TRUNC('MONTH',CURRENT_DATE);
#   '''


#index= count()

# fig2=plt.figure()
#df=fig
# dataf2=fig.add_subplot()  
#df=pd.read_sql_query(query, engine)
#df1=pd.read_sql_query(query2, engine)
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

def animate(i):
    test1 = widgets.Output()
    test2 = widgets.Output()
    df=pd.read_sql_query(query, engine)
    df1=pd.read_sql_query(query2, engine)
    
    tab = widgets.Tab(children = [test1, test2])
    tab.set_title(0, '1 Month')
    tab.set_title(1, '6 Month')
    display(tab)
          
    with test1:
        
        plt.cla()
        df.set_index(['trade_date'], inplace=True)
        #fig1, ax1 = plt.subplots()
       
        #ax1.plot(df[['low','high']])
        
        df.plot(ax = ax1)
        plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(6))#c
        #ax1.legend()
        plt.title('DIH Stock data')
        plt.xlabel('Date')
        plt.ylabel('Stock Price')
        #plt.pause(0.0001)
        #plt.show ()
        #print(df.head(10))
        #plt.show() 
        
        # #plt.cla()
        # df.set_index(['trade_date'], inplace=True)
        # dArray=df.split('\n')
        # xval=[]
        # yval=[]
        
        # for line in dArray:
        #     if len(line)>1:
        #         x,y=line.split(',')
        #         xval.append(int(x))
        #         yval.append(int(y))
                
        # ax1.cla()
        # ax1.plot(xval,yval)
        
      
        
    with test2:
        plt.cla()
        df1.set_index(['trade_date'], inplace=True)
        #fig2, ax2 = plt.subplots()
        
        #ax2.plot(df1[['high']]) #plots it without legends, hence query has to be exactly what yu want
        
        df1.plot(ax = ax2)
        plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(6))#c
        #plt.legend()
        plt.title('DIH Stock data')
        plt.xlabel('Date')
        plt.ylabel('Stock Price')
        #plt.show()
    
#return df,df1,
    #plt.pause(0.0001)

#plt.show()
    #plt.pause(0.0001)

anim=FuncAnimation(plt.gcf(), animate, interval=1000)        

#ani=animation.FuncAnimation(plt.gcf(), animate, init_func=init, interval=1000, blit=True)
#plt.tight_layout()
plt.show() 
#------
        # #plt.cla()
        # df.set_index(['trade_date'], inplace=True)
        
        # fig1, ax1 = plt.subplots()
        # #ax1.plot(df[['low','high']])
        # #plt.cla()
        # dArray=df.split('\n')
        # xval=[]
        # yval=[]
        
        # for line in dArray:
        #     if len(line)>1:
        #         x,y=line.split(',')
        #         xval.append(int(x))
        #         yval.append(int(y))
                
        # ax1.clear()
        # ax1.plot(xval,yval)
        
        # df.plot(ax = ax1)
        # plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(6))#c
        # #ax1.legend()
        # plt.title('DIH Stock data')
        # plt.xlabel('Date')
        # plt.ylabel('Stock Price')



# def init():
#     df.set_index(['trade_date'], inplace=True)
#     df1.set_index(['trade_date'], inplace=True)
#     return df,df1,

# def animate(i):
#     test1 =widgets.Output()
#     test2 =widgets.Output()
#     df=pd.read_sql_query(query, engine)
#     df1=pd.read_sql_query(query2, engine)
    
#     tab=widgets.Tab(chidren=[test1, test2])
#     tab.set_title (0, '1 Month')
#     tab.set_title (1, '6 Month')
#     display(tab)
    
#     with test1:
#         #df=pd.read_sql_query(query, engine)
#         df.set_index(['trade_date'], inplace=True)
#         #plt.cla() 
#         #plt.ion()
#         df[['low','high']].plot(title='DIH Stock data')
#         plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(6))#c
#         plt.legend()
#         plt.xlabel('Date')
#         plt.ylabel('Stock Price')
#         #plt.show()
#         #print(df.head(10))

#         #plt.pause(0.0001)
    
#     with test2:
#         #df=pd.read_sql_query(query2, engine)
#         df1.set_index(['trade_date'], inplace=True)
#         #plt.ion()
#         df1[['high']].plot(title='DIH Stock data')
#         plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(6))#c
#         plt.legend()
#         plt.xlabel('Date')
#         plt.ylabel('Stock Price')
#         #plt.show()
#         #plt.pause(0.0001)
#     return df,df1,
#-----    
      
    # with test1:
    #     #plt.cla()
    #     #df.set_index(['trade_date'], inplace=True)
    #     plt.ion()
    #     fig1, ax1 = plt.subplots()
    #     ax1.plot(df[['low','high']])
    #     plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(6))#c
    #     #ax1.legend()
    #     plt.title('DIH Stock data')
    #     plt.xlabel('Date')
    #     plt.ylabel('Stock Price')
    #     plt.pause(0.0001)

    #     #plt.show()
    #     #print(df.head(10))
    #     #plt.tight_layout()
    
    # with test2:
    #     #plt.cla()
    #     plt.ion()
    #     fig2, ax2 = plt.subplots()
    #     ax2.plot(df1[['high']])
    #     plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(6))#c
    #     #plt.legend()
    #     plt.title('DIH Stock data')
    #     plt.xlabel('Date')
    #     plt.ylabel('Stock Price')
    #     #plt.show()
    #     plt.pause(0.0001)

        
#-------

# #%matplotlib inline
# import pandas as pd
# import pandas_datareader as pdr
# import datetime as dt
# import matplotlib.pyplot as plt
# from matplotlib.pyplot import style
# import matplotlib.ticker as mticker
# import psycopg2 as pg2
# import sqlalchemy 
# import matplotlib.animation as animation
# #from matplotlib.finance import candlestick_ohlc
# import ipywidgets as widgets
# from itertools import count


# style.use ("ggplot")
# engine= sqlalchemy.create_engine('postgresql://postgres:SimplePW1@localhost:5432/GASCI')

# query ='''Select trade_date, low, high FROM dihtradedata
# WHERE trade_date>CURRENT_DATE - interval '31' day;''' 
# #Looks for the last 31 days of data from the current date

# query2 ='''SELECT trade_date, low, high FROM dihtradedata 
# WHERE trade_date BETWEEN '2019-04-01' AND '2019-04-30' '''
# #df=pd.read_sql_query(query, engine)

# # query ='''SELECT trade_date, low, high
# # FROM dihtradedata 
# # WHERE DATE_TRUNC('MONTH', trade_date) = DATE_TRUNC('MONTH',CURRENT_DATE);
# #   '''


# #index= count()

# # fig2=plt.figure()
# #df=fig
# # dataf2=fig.add_subplot()  

# # df=plt.figure()
# # df1=plt.figure()
# df=pd.read_sql_query(query, engine)
# df1=pd.read_sql_query(query2, engine)

# def init():
#     df.set_index(['trade_date'], inplace=True)
#     df1.set_index(['trade_date'], inplace=True)
#     return df,df1,

# # init_func=init
# # init()

# def animate(i):
#     test1 =widgets.Output()
#     test2 =widgets.Output()
#     tab=widgets.Tab(chidren=[test1, test2])
#     tab.set_title (0, '1 Month')
#     tab.set_title (1, '6 Month')
#     display(tab)
    
#     with test1:
#         #df=pd.read_sql_query(query, engine)
#         # df.set_index(['trade_date'], inplace=True)
#         #plt.cla() 
#         #plt.ion()
#         df[['low','high']].plot(title='DIH Stock data')
#         plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(6))#c
#         plt.legend()
#         plt.xlabel('Date')
#         plt.ylabel('Stock Price')
#         #plt.show()
#         #print(df.head(10))
#         #plt.pause(0.0001)
    
#     with test2:
#         #df=pd.read_sql_query(query2, engine)
#         #df1.set_index(['trade_date'], inplace=True)
#         #plt.ion()
#         df1[['high']].plot(title='DIH Stock data')
#         plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(6))#c
#         plt.legend()
#         plt.xlabel('Date')
#         plt.ylabel('Stock Price')
#         #plt.show()
#         #plt.pause(0.0001)
#     return df,df1,

# animate(1)
# --------------------
##pulls data to graph
# test1 =widgets.Output()
# test2 =widgets.Output()
# df=pd.read_sql_query(query, engine)
# df1=pd.read_sql_query(query2, engine)

# tab=widgets.Tab(chidren=[test1, test2])
# tab.set_title (0, '1 Month')
# tab.set_title (1, '6 Month')
# display(tab)
    
# with test1:
#     #df=pd.read_sql_query(query, engine)
#     df.set_index(['trade_date'], inplace=True)
#     df[['low','high']].plot(title='DIH Stock data')
#     plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(6))#c
#     plt.legend()
#     plt.xlabel('Date')
#     plt.ylabel('Stock Price')
#     plt.show()
#     print(df.head(10))

# with test2:
#     #df=pd.read_sql_query(query2, engine)
#     df1.set_index(['trade_date'], inplace=True)
#     df1[['high']].plot(title='DIH Stock data')
#     plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(6))#c
#     plt.legend()
#     plt.xlabel('Date')
#     plt.ylabel('Stock Price')
#     plt.show()

#.....................
   
# test1 =widgets.Output()
# test2 =widgets.Output()
# #dataf1=pd.read_sql_query(query, engine)
# #dataf2=pd.read_sql_query(query, engine)

# tab=widgets.Tab(chidren=[test1, test2])
# tab.set_title (0, '1 Month')
# tab.set_title (1, '6 Month')
# display(tab)
    
# with test1:
#     df=pd.read_sql_query(query, engine)
#     df.set_index(['trade_date'], inplace=True)
#     df[['low','high']].plot(title='DIH Stock data')
#     plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(6))#c
#     plt.legend()
#     plt.xlabel('Date')
#     plt.ylabel('Stock Price')
#     plt.show()
#     print(df.head(10))

# with test2:
#     df=pd.read_sql_query(query2, engine)
#     df.set_index(['trade_date'], inplace=True)
#     df[['high']].plot(title='DIH Stock data')
#     plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(6))#c
#     plt.legend()
#     plt.xlabel('Date')
#     plt.ylabel('Stock Price')
#     plt.show()

#...................        
        
# df=pd.read_sql_query(query, engine)
# df.set_index(['trade_date'], inplace=True)
# df[['low','high']].plot(title='DIH Stock data')
# plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(6))#c
# plt.legend()
# plt.xlabel('Date')
# plt.ylabel('Stock Price')
# #plt.title('DIH Stock data')
# plt.show()
# print(df.head(10))


