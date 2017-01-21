# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 12:09:41 2017

@author: 张瑞
"""

def proc(n ):
    if (n<0):
        print '-', 
        n = -n
    if (n / 10):
        proc(n / 10 )
    print n % 10,

proc(-345 )