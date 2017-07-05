# -*- coding: utf-8 -*-
def fib(max):
	a, b, n = 0, 1, 0
	while n < max:
		print b
		a, b = b, a+b
		n = n + 1


fib(6)