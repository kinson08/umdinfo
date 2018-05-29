# -*- coding: utf-8 -*-
"""
Created on Sun May 20 22:33:50 2018
获得所有股票的概念、地域综合信息
@author: kinso
"""

import numpy as np
import pandas as pd
import tushare as ts
from pandas import Series,DataFrame
import stockstats as ss
from stockstats import StockDataFrame
import datetime,math

pd.set_option('display.max_rows',20)

stock_concept=ts.get_concept_classified()
print('stock_concept:%i'%(len(stock_concept)))

#concept_count=concept_all.groupby('c_name')['code'].count()
#pd.set_option('display.max_columns',None)
stock_area=ts.get_area_classified()
print('stock_area:%i'%(len(stock_area)))

stock_industry=ts.get_industry_classified()
print('stock_industry:%i'%(len(stock_industry)))

stock_sme=ts.get_sme_classified()
stock_sme['type']='中小板'
print('stock_sme:%i'%(len(stock_sme)))

stock_df=pd.merge(stock_concept,stock_area,on=['code','name'],how='outer')
stock_df=pd.merge(stock_df,stock_industry,on=['code','name'],how='outer')
stock_df=pd.merge(stock_df,stock_sme,on=['code','name'],how='outer')
#print(concept_count.sort_values())
