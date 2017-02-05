# -*- coding: utf-8 -*-
"""
Created on Sun Feb 05 20:01:19 2017

@author: 张瑞
"""

from pandas import *
Uname=['zhangrui','wangshao','zhouyue','shouyi','liuyao','lisicheng','jiyanping']
salary=[5000,20000,12000,14000,10000,60000,10000]
Uname_salary_dic=dict(zip(Uname,salary))
#Uname_salary_dataFrm=pandas.DataFrame(Uname_salary_dic)
print Uname_salary_dic


data={'name':['zhangrui','jk','zr'],'scores':[100,90,80]}
frame=pandas.DataFrame(data)
print 'frame:','\n',frame
print '''frame['name']:''','\n',frame['name']
print 'frame.name:','\n',frame.name
print '''frame.['scores']:''','\n',frame['scores']
print 'frame.ix[0]:','\n',frame.ix[0]
