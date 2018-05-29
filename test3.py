# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:59:23 2018

@author: kinso
"""
import math
import tushare as ts
import numpy as np
from pandas import Series,DataFrame
import pandas as pd
import stockstats as ss
from stockstats import StockDataFrame
import matplotlib.pyplot as plt 

#%%
df=ts.get_k_data('600470',ktype='D')
sdf=StockDataFrame.retype(df)
#sdf[['close','boll','boll_ub','boll_lb']].plot(figsize=(20,10),grid=True)

sdf[['close','cr']].tail(500).plot(figsize=(20,10),grid=True,subplots=True)
plt.text(0,1,sdf['cr'].tail(40))
plt.show()

#%%
#寻找CR的峰值和谷値
peak_valley=DataFrame(columns=test_data1.columns)
peak_valley['peak']=''
test_data1=sdf.tail(500)
wave_len=15

for n in range(math.ceil(len(test_data1)/wave_len)):    
    start_pos=n*wave_len
    temp_data=test_data1[start_pos:start_pos+wave_len]
    max_cr=temp_data[temp_data.cr==max(temp_data.cr)]
    max_cr['peak']='max'
    min_cr=temp_data[temp_data.cr==min(temp_data.cr)]
    min_cr['peak']='min'
    
    if len(peak_valley)==0:#empty in dataframe
        if max_cr.index>min_cr.index:#min--max
            peak_valley=peak_valley.append([min_cr,max_cr])
        else:#max--min
            peak_valley=peak_valley.append([max_cr,min_cr])
    else:#not empty in peak dataframe
        last_cr=peak_valley.tail(1)
        if max_cr.index>min_cr.index:# min---max
            if last_cr['peak'][0]=='max':#last is max
                if min_cr['cr'][0]<last_cr['cr'][0]:#curr min <last max
                    peak_valley=peak_valley.append([min_cr,max_cr])#max-min-max
                else:#curr min>last max
                    peak_valley=peak_valley.drop(peak_valley.index[len(peak_valley)-1])
                    peak_valley=peak_valley.append(max_cr)#max
            else:#last is min
                if min_cr['cr'][0]<last_cr['cr'][0]:#curr min <last min
                    peak_valley=peak_valley.drop(peak_valley.index[len(peak_valley)-1])
                    peak_valley=peak_valley.append([min_cr,max_cr])#min-max
                else:#curr min>last min
                    peak_valley=peak_valley.append(max_cr)#min-max
        else:# max--min
            if last_cr['peak'][0]=='max':#last is max
                if max_cr['cr'][0]<last_cr['cr'][0]:#curr max <last max
                    peak_valley=peak_valley.append(min_cr)#max-min
                else:#curr max >last max
                    peak_valley=peak_valley.drop(peak_valley.index[len(peak_valley)-1])
                    peak_valley=peak_valley.append([max_cr,min_cr])#max-min
            else:#last is min
                if max_cr['cr'][0]<last_cr['cr'][0]:#curr max <last min
                    peak_valley=peak_valley.drop(peak_valley.index[len(peak_valley)-1])
                    peak_valley=peak_valley.append(min_cr)#min
                else:#curr max >last min
                    peak_valley=peak_valley.append([max_cr,min_cr])#min-max-min
#    print(peak_valley.peak)
                        
#%%
    peak_valley.cr.plot()
