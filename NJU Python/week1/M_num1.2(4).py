# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 12:22:49 2017

@author: 张瑞
"""
import math

def isprime(x):
    'judge whether a prime number'
    sqnum=int(math.sqrt(x))
    i=1
    for i in range(2,sqnum+1):
        if x%i==0:
            return False
    return True


def isMonisen():
    print 'P M'
    count=0
    p=2
    while 1:
        if isprime(p):
            m=2**p-1
            if isprime(m):
                print p,m
                count=count+1
                if count==5:
                    break
        p=p+1

isMonisen()