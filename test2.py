# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 17:13:12 2017

@author: 张瑞
"""

def f(x,y=True):
    if y:
        print x,'and y'
    print x
f(y=False,x=1000)
'f(33,False)'