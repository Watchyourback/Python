# -*- coding: utf-8 -*-
"""
Created on Sun Feb 05 16:30:59 2017

@author: 张瑞
"""

import numpy as np

xArray =np.ones((3,3))
print xArray


from scipy import linalg
arr=np.array([[1,2],[3,4]])
print arr,linalg.det(arr)

from numpy import *

aArray=array([(1,2,3)])

bArray=array([(1,2,3),(3,4,5)])
print bArray,'\n',bArray
print bArray.sum(axis=1)
print bArray.sum(axis=0)