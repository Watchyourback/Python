# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 21:44:07 2017

@author: 张瑞
"""

'''将字符串的“hello world”换成“Python”并计算其中的标点个数'''

str1='hello,world!'
str2=str1[:7]+'Python!'
ct=0
for char in str2:
    if char in ',.?!':
        ct=ct+1
print 'punctuation marks=%d'%(ct)
    