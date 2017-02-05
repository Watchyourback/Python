# -*- coding: utf-8 -*-
"""
Created on Sun Feb 05 17:19:58 2017

@author: 张瑞
"""
from pandas import *
aser=pandas.Series([1,2.0,'a'])
print aser

bser=pandas.Series(['zhangrui','jack','jackey'],index=[1,2,3])
print bser,'\n',bser[2]