# -*- coding: utf-8 -*-
"""
Created on Sun May 20 08:35:53 2018
回测一直股票CR指标买入的胜率分析
@author: kinso
"""

import numpy as np
import pandas as pd
import tushare as ts
from pandas import Series,DataFrame
import stockstats as ss
from stockstats import StockDataFrame
import datetime,math


def test_cr(stock_code,day_range):
#%%  
#    stock_code='600470'
#    day_range=5

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
    print('='*40)
    print('The success rate for %s is %4.2f%%.'%(stock_code,100*len(cr_result[cr_result.max_profit>0])/len(cr_result)))
    print('-'*40)

#%%
    return(cr_result.describe()[['cr','max_profit','max_day']])

#%%

if __name__=='__main__':
    cr_result=test_cr('600598',5)
    print(cr_result)
    print('='*40)
    
    
