# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 11:48:18 2017

@author: 张瑞
"""

import math
def fun(num):
    if num<0:
        print '-',
        num = -num
    if num/10:
        fun(num/10)
    print chr(num%10+48),
a=input()
fun(a)