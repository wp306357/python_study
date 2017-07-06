# -*- coding: utf-8 -*-
print u'斐波拉契数列(Fibonacci)'
def fib(max):
	a, b, n = 0, 1, 0
	while n < max:
		print b
		a, b = b, a+b
		n = n + 1
fib(6)

print u'利用for循环遍历generator生成器的值'
group = (x*x for x in range(10))
#print group.next()
for d in group:
	print d

print u'利用yield将斐波拉契数列变成generator生成器'
def yield_fib(yield_max_num):
	n, a, b = 0, 0, 1
	while n < yield_max_num:
		yield b
		a, b = b, a+b
		n = n + 1
for d in yield_fib(9):
	print d