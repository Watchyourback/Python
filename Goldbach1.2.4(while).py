# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 12:26:52 2017

@author: 张瑞
"""
import math
i=2
while i<1000:
    j=2
    k=math.sqrt(i)
    while j<=k:
        if i%j==0:
            break
        j=j+1
    if j>k:
        print i,
    i+=1