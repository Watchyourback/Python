# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 22:23:43 2017

@author: 张瑞
"""

'''判断双引号中的词是否是标题格式"No pains,No gains"  '''


str='snjnsjknsksmkl"No pains,No gains"'
tempstr=str.split('"')[1]
if tempstr.istitle():
    print 'is title format'
else:
    print 'not title format'
print tempstr.title()