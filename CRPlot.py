# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:59:23 2018
显示单只股票的CR和收盘价趋势图，近期CR数值。
@author: kinso
"""

import tushare as ts
import numpy as np
from pandas import Series,DataFrame
import pandas as pd
import stockstats as ss
from stockstats import StockDataFrame
import matplotlib.pyplot as plt 


df=ts.get_k_data('600598',ktype='D')
sdf=StockDataFrame.retype(df)
#sdf[['close','boll','boll_ub','boll_lb']].plot(figsize=(20,10),grid=True)
sdf[['close','cr']].tail(500).plot(figsize=(20,10),grid=True,subplots=True)
plt.text(0,1,sdf['cr'].tail(40))
plt.show()

