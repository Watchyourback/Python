# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 17:20:35 2017

@author: 张瑞
"""


from math import sqrt
def isprime(x):
    'check wether prime num 2~100'
    k=int(sqrt(x))
    flag=False;
    for j in range(2,k+1):
        if x%j==0:
            flag=0
            break
        flag=1
    return flag
for i in range(2,101):
    if(isprime(i)):
        print i,