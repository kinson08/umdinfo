# -*- coding: utf-8 -*-
"""
Created on Sun May 20 22:33:50 2018
获得概念分类名称及其股票数量
@author: kinso
"""

import numpy as np
import pandas as pd
import tushare as ts
from pandas import Series,DataFrame
import stockstats as ss
from stockstats import StockDataFrame
import datetime,math


concept_all=ts.get_concept_classified()
concept_count=concept_all.groupby('c_name')['code'].count()
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)

print(concept_count.sort_values())
