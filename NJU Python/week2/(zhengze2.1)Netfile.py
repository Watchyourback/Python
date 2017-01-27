# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 13:07:56 2017

@author: 张瑞
"""

import urllib2
import re
dStr = urllib2.urlopen('https://hk.finance.yahoo.com/q/cp?s=%5EDJI').read()
m = re.findall('<tr><td class="yfnc_tabledata1"><b><a href=".*?">(.*?)</a></b></td><td class="yfnc_tabledata1">(.*?)</td>.*?<b>(.*?)</b>.*?</tr>', dStr)
if m:
    print m
    print '\n'
    print len(m)
else:  
    print 'not match'