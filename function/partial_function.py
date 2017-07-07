# -*- coding: utf-8 -*-
print u'偏函数'

#引入functools模块
import functools
int2 = functools.partial(int, base=2)
int3 = functools.partial(int, base=8)
print int2('10011101')
print int3('123')

max2 = functools.partial(max, 10)

print max2(1,2,3)