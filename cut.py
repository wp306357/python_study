# -*- coding: utf-8 -*-
L = ['2','3','555','333']
print "sss %s" % (L[:2])

d = {'a':1, 'b':2, 'c':3}
for key in d:
	print key

for val in d.itervalues():
	print val

for key,val in d.iteritems():
	print key, val

print u'使用isinstance检验是否可迭代'
from collections import Iterable
print isinstance('abc', Iterable)

#Python内置的enumerate函数可以把一个list变成索引-元素对
list = ['A', 'B', 'C']
for i, value in enumerate(list):
	print i, value
	print list[i]
	
#birth = int(raw_input('birth:'))
birth = 1991
if birth < 2000:
	print u'00前'
else:
	print u'00后'

for x,y in [(1,1), (2,3), (4,5)]:
	print x,y

print u'enumerate函数使用打印index, value'
for index, value in enumerate([1,2,3]):
	print index, value
