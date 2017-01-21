# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 11:12:40 2017

@author: 张瑞
"""

score=input('Please input scores: ')
if score>=90 and score<=100:
    print 'A'
elif score>=80 and score<90:
    print 'B'
elif score>=70 and score<80:
    print 'C'
elif score>=60 and score<70:
    print 'D'
else:
    print 'Invalid score'