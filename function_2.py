# -*- coding: utf-8 -*-
def power(x):
	return x*x

print power(2)

def power2(x, n=2):
	s = 1
	while n > 0:
		n = n -1
		s = s * x
	return s

print power2(3)
print power2(3,3)

def add_end(L = None):
	if(L == None):
		L = []
	L.append('END')
	return L

print add_end()
print add_end()

def cals(*numbers):
	sum = 0
	for number in numbers:
		sum = sum + number
	return sum

print cals(1,2,3)
print cals(1,2)

num = [2,3,4]
print cals(*num)

def person(name, age, **kw):
	print 'name:', name, 'age:', age, 'other:', kw

person('moben', 26, lover='Lin', time=1314)
person('moben', 26, lover='Lin')

kw = {'lover':'Lin', 'gender':u'女'}
person('moben',26, **kw)


#利用尾递归方法解决递归方法常出现的堆栈溢出问题
def fact(n):
	return fact_iter(n, 1)

def fact_iter(num, sum):
	if(num == 1):
		return sum
	return fact_iter(num - 1, num * sum)

print fact_iter(6, 1)
print fact(6)