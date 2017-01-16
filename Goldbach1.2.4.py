# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 11:47:02 2017

@author: 张瑞
"""

from math import sqrt
i=2
while i<=100:
    j=2
    k=sqrt(i)
    while(j<=k):
        if i%j==0:
            break
        j=j+1
    if j>k:
        print i,
    i=i+1