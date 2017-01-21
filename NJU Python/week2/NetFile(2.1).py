# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 12:55:17 2017

@author: 张瑞
"""

import urllib
r=urllib.urlopen('http://z.cn/')
html=r.read()
print html