# -*- coding: utf-8 -*-
"""
Created on Sat May 12 18:13:46 2018

@author: kinso
"""
import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import tushare as ts
text=list()
mynews=ts.get_latest_news(top=20,show_content=True)
mykeyword=['芯片','自动驾驶','钛白粉','动车','边缘','分析']

#%%
for n in range(len(mynews)):
    title_str=mynews.loc[n]['title']
    content_str=mynews.loc[n]['content']
    for kw in mykeyword:
        if title_str.find(kw)>=0:
            print('---> '+title_str)
            print('['+content_str+']\n')
            break

        
        
