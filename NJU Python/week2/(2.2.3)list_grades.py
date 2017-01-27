# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 22:43:59 2017

@author: 张瑞
"""

judge_list=[9,9,8.5,10,7,8,8,9,8,10]
judge_list.sort()
judge_list.pop()
judge_list.pop(0)
audience_list=9
judge_list.append(audience_list)
print judge_list
print sum(judge_list)/len(judge_list)