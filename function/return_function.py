# -*- coding: utf-8 -*-
print u'返回函数'
def lazy_sum(*num):
	def self_sum():
		total = 0
		for x in num:
			total = total + x
		return total
	return self_sum

f = lazy_sum(1,2,3,4)
print f

print f()


print u'闭包'
def count():
	fs = []
	for i in range(1, 4):
		def f():
			return i * i
		fs.append(f)
	return fs

f1,f2,f3 = count()

print f1()
print f2()
print f3()

print u'已绑定到函数参数的值不变'
def new_count():
	fs = []
	for i in xrange(1,4):
		def f(j):
			def g():
				return j * j
			return g
		fs.append(f(i))
	return fs

f4,f5,f6 = new_count()

print f4()
print f5()
print f6()

print u'匿名函数'
print map(lambda x: x * x, [1,2,3,4])

print u'匿名函数也是一个变量'
f = lambda x,y: x + y
print f(7,8)

def build(x, y):
	return lambda x,y: x * x + y * y

lambdaFuntion = build(7,8)
print lambdaFuntion(5,6)
