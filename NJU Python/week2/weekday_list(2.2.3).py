# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 22:59:51 2017

@author: 张瑞
"""

week_list=['monday','tuesday','wednesday','thursday','friday']
weekend_list=['saturday','sunday']
week_list.extend(weekend_list)
week_list_daynum=len(week_list)
'enmerate(week_list)'
i=0
for i in range(week_list_daynum):
    print i+1,week_list[i]