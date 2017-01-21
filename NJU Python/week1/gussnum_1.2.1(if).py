# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 18:28:28 2017

@author: 张瑞
"""

#Filename:guessnum.py
from random import randint
rannum=randint(0,10)
print rannum
usernum=raw_input('please input your guess number ')
if rannum==usernum:
    print'bingo'
elif usernum<rannum:
    print'samll try again'
else:
    print'big try again'