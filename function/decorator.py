# -*- coding: utf-8 -*-
print u'装饰器'

def log(func):
	def warpper(*arg, **args):
		print 'execute %s' % func.__name__
		return func(*arg, **args)
	return warpper

@log
def now():
	print '2017-07-07'

now()
print u'now函数的__name__已被修改为: %s' % now.__name__

import functools
def newLog(text):
	def selfDecorator(func):
		@functools.wraps(func)
		def warpper(*arg, **args):
			print '%s %s' % (text, func.__name__)
			return func(*arg, **args)
		return warpper
	return selfDecorator

@newLog('exect function')
def newNow():
	print u'新的装饰器'

newNow()
print u'newNow函数的__name__保存原样为: %s' % newNow.__name__


print u'请编写一个decorator，能在函数调用的前后打印出begin call和end call的日志。'

def myLog(text):
	def myDecorator(func):
		@functools.wraps(func)
		def warpper(*k, **km):
			print 'begin call %s %s' % (func.__name__, text)
			result = func(*k, **km)
			print 'end call %s %s' % (func.__name__, text)
			return result
		return warpper
	return myDecorator

@myLog("()")
def test():
	print u'装饰器练习题'

test()
print test.__name__



