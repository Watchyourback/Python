# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 14:52:17 2017

@author: 张瑞
"""

from math import sqrt
for i in range (2,101):
    k=int(sqrt(i))
    for j in range (2,k+1):
        if(i%j)==0:
            break
    if (j+1>k):
        print i,