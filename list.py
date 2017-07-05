# -*- coding: utf-8 -*-
print [x*x for x in xrange(0,10)]
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print [x * x for x in xrange(0,100) if x%10==0]
#[0, 100, 400, 900, 1600, 2500, 3600, 4900, 6400, 8100]

print [m + n for m in 'ABC' for n in 'DEF']
#['AD', 'AE', 'AF', 'BD', 'BE', 'BF', 'CD', 'CE', 'CF']

print [v1 + v2 for index1,v1 in enumerate('ABC') for index2,v2 in enumerate('DEF') if index1 == index2]
#['AD', 'BE', 'CF']

import os # 导入os模块，模块的概念后面讲到
print [d for d in os.listdir('.')] # os.listdir可以列出文件和目录

tempList = ["HELLO", "WORLD"]
print [s.lower() for s in tempList]