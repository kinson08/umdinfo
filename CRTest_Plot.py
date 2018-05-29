# -*- coding: utf-8 -*-
"""
Created on Sun May 20 08:35:53 2018
回测多只股票CR指标指定周期下的胜率比较
@author: kinso
"""

import numpy as np
import pandas as pd
import tushare as ts
from pandas import Series,DataFrame
import stockstats as ss
from stockstats import StockDataFrame
import matplotlib.pyplot as plt 
import datetime,math

#%%
def test_cr(stock_code):
#%%  
#    stock_code='600470'
    day_range=5

    df=ts.get_k_data(stock_code)
    s_df=StockDataFrame.retype(df.tail(400))
    
    day_str_list=list()
    for n in range(day_range):
        day_str_list.append('close_%d_r'%(n+1))
        
    s_cr=s_df[['close','cr']+day_str_list]

    #统计期限内的最高收益值    
    s_cr['max_profit']=s_cr[day_str_list].max(axis=1)
    
    #统计期限内出现最高收益值的列，并提取天数数据，转换成浮点类型，增加一列。
    s_cr['max_col']=s_cr[day_str_list].idxmax(axis=1)
    s_cr['max_day']=s_cr['max_col'].str.split('_',expand=True)[1].astype(float)
    
    #提取有用的列和数据（CR<25%时的收盘价、最高收益和最高收益天数)
    cr_result=s_cr[s_cr.cr<s_cr.cr.describe()['25%']][['close','cr','max_profit','max_day']]
        
    #计算收益大于0的成功率
#    print('%s-->%4.2f%%'%(stock_code,100*len(cr_result[cr_result.max_profit>0])/len(cr_result)))
#%%
    if s_cr.tail(1).cr[0]<s_cr.cr.describe()['25%']:#当前的CR値低于25%
#        print(s_cr.tail(1).cr[0])
        return(100*len(cr_result[cr_result.max_profit>0])/len(cr_result))
    else:
#        print('-'*20)
        return(0)

def stock_plot(code):
#    code='002426'
    df=ts.get_k_data(code,ktype='D')
    sdf=StockDataFrame.retype(df)
    #sdf[['close','boll','boll_ub','boll_lb']].plot(figsize=(20,10),grid=True)
    sdf[['close','cr']].tail(500).plot(figsize=(20,10),grid=True,subplots=True)
    plt.text(0,1,sdf['cr'].tail(40))
    plt.title(code)
    plt.show()


if __name__=='__main__':    
    concept='云计算'
    concept_all=ts.get_concept_classified()
#    print(concept_all.groupby('c_name')['code'].count())
    concept_df=concept_all[concept_all.c_name==concept]
#    concept_df=ts.get_hs300s()
    concept_df['rate']=concept_df['code'].map(test_cr)
    concept_df=concept_df.sort_values('rate')
#    print(concept_df)
    #%%
    for n in concept_df[concept_df['rate']>70]['code']:
        stock_plot(n)
    
    
    
    