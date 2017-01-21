# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 13:28:16 2017

@author: 张瑞
"""
'''question 
编程小练习（不计分）

请完成以下文件综合编程迷你项目（提示：可以利用list的insert函数）。 

(1) 创建一个文件Blowing in the wind.txt，其内容是： 

How many roads must a man walk down 

Before they call him a man 

How many seas must a white dove sail 

Before she sleeps in the sand 

How many times must the cannon balls fly 

Before they're forever banned 

The answer my friend is blowing in the wind 

The answer is blowing in the wind 

(2) 在文件头部插入歌名“Blowin’ in the wind” 

(3) 在歌名后插入歌手名“Bob Dylan” 

(4) 在文件末尾加上字符串“1962 by Warner Bros. Inc.” 

(5) 在屏幕上打印文件内容
'''


# (1)写入歌词#

f1=open(r'E:\Blowing in the wind.txt','w')
f1.write('How many roads must a man walk down \n')
f1.write('Before they call him a man \n')
f1.write('How many seas must a white dove sail  \n')
f1.write('Before she sleeps in the sand  \n')
f1.write('How many times must the cannon balls fly  \n')
f1.write('Before they\'re forever banned \n')
f1.write('The answer my friend is blowing in the wind \n')
f1.write('The answer is blowing in the wind \n')
f1.close()


#(2)插入歌名#

f2=open(r'E:\Blowing in the wind.txt','r+')
songname='Blowin in the wind \n'
songstr=f2.readlines()
songstr.insert(0,songname)
f2.seek(0,0)
f2.writelines(songstr)
f2.close()



#（3）歌名后面插入歌手名#

f3=open(r'E:\Blowing in the wind.txt','r+')
songsinger='Bob Dylan \n'
songstr=f3.readlines()
songstr.insert(1,songsinger)
f3.seek(0,0)
f3.writelines(songstr)
f3.close()

#(4) 在文件末尾加上字符串“1962 by Warner Bros. Inc.” #
etcinfor='1962 by Warner Bros. Inc.'
f4=open(r'e:\Blowing in the wind.txt','a+')
f4.writelines(etcinfor)
f4.seek(0,0)
f4.close()
#(5)屏幕上打印#

f_read=open(r'E:\Blowing in the wind.txt','r')
songstr=f_read.readlines()
print songstr
f_read.close()