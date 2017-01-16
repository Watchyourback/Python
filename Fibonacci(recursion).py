# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 20:07:32 2017

@author: 张瑞
"""

def fibonacci(x):
    if x==0 or x==1:
        return x
    else:
        return fibonacci(x-1)+fibonacci(x-2)
num=input()
print fibonacci(num)
