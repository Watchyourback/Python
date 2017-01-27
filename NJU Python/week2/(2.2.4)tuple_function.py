# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 16:06:54 2017

@author: 张瑞
"""

def fun(a,*ab):
    print a
    print ab
print fun('hello','a','b','c','1')


def fun1():
    return 1,2,3
print fun1()