# -*- coding: utf-8 -*-
print type(1232)

print dir("ABC")

print ','.join("avn")

class Student(object):
	__slots__ = ('name','age')

s = Student()
s.name = 'moben'

print s.name

print u'__slots__变量中未定义score属性，动态绑定score属性报错'
#__slots__变量中未定义score属性，动态绑定score属性报错
s.score = 99 