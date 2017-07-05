# -*- coding: utf-8 -*-
print "function!"

def power(x, n=3):
	s = 1
	while n > 0:
		s = s*x
		n = n-1
	return s

print 'enter your number'
a = raw_input()
print 'your number is : %d' % (power(int(a)))

def add_end(L=None):
	if L is None:
		L = []
	L.append('End')
	return L
	
print 'result str: %s' % (add_end([1,2,3]))
print 'result str: %s' % (add_end())

#会产生堆栈溢出问题
def fact(n=5):
	if n == 1:
		return 1
	return n * fact(n - 1)
print 'result %d' % (fact())

def new_fact_do(n = 5):
	return new_fact(n, 1)
def new_fact(num, product):
	if num == 1:
		return product
	return new_fact(num-1, num*product)

print 'result2 %d' % (new_fact_do())