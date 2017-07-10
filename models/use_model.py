# -*- coding: utf-8 -*-

'a model test'
__author__ = 'Moben'

import sys

def test():
	args = sys.argv
	if(len(args) == 1):
		print 'Hello World'
	elif(len(args) == 2):
		print 'hello %s' % args[1]
	else:
		print 'too many args'

if __name__ == '__main__':
	test()

print u'别名'
try:
	import cStringIO as StringIO
except ImportError:
	import StringIO

try:
	import json
except ImportError:
	import simplejson as json

def _private1(name):
	print 'hello, %s' % name

def _private2(name):
	print 'hi, %s' % name

def greet(name):
	if(len(name) > 3):
		return _private1(name)
	else:
		return _private2(name)

greet('moben')
