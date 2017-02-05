# -*- coding: utf-8 -*-
"""
Created on Sun Feb 05 16:33:13 2017

@author: 张瑞
"""
from numpy import *
def fun(x,y):
    return (x+1)*(y+1)
arr=fromfunction(fun,(9,9))
print arr


'''def fun2(z,):

    return z+1
arr2=fromfunction(fun2,(3,3))
print arr'''