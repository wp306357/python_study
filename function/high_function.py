# -*- coding: utf-8 -*-
def add(x, y, f):
	return f(x) + f(y)

print add(-8, 2, abs)

print u'map/reduce函数练习题:'
print u'练习利用map()函把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：["adam", "LISA", "barT"]，输出：["Adam", "Lisa", "Bart"]。'
print u'Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积。'

print u'map练习题:'
oldNameList = ['adam', 'LISA', 'barT']
def my_name(old_name):
	d = []
	for index, value in enumerate(old_name):
		if(index == 0):
			d.append(value.upper())
		else:
			d.append(value.lower())
	return ''.join(d)

#print my_name('adam')
print map(my_name, oldNameList)

print u'reduce练习题:'
numberList = [1,2,3,5,6]
def prod(*number):
	def fn(x, y):
		return x * y
	return reduce(fn, *number)

print prod(numberList)

print u'map(函数，计算值) 与 reduce(函数, 计算值)'

print u'map练习题网络答案:'
def normalize(s):
	if not isinstance(s, str):
		raise TypeError('input is not string')
	if len(s) < 2:
		raise TypeError('The name is too short')
	return (s[0].upper() + s[1:].lower())

print normalize('barT')
print map(normalize, oldNameList)

def ss(s1):
	return s1[0].upper() + "ss" + s1[1:].lower()
print map(ss, oldNameList)

print u'filter()练习题:'
print u'请尝试用filter()删除1~100的素数。'
def prime(num):
	result, n = True, 2
	while (n < num):
		if(num % n == 0):
			result = False
		n = n + 1
	return result

print filter(prime, range(1,101))

print u'sorted()函数使用:'
def revered_cmp(x, y):
	if (x < y):
		return 1
	elif (x > y):
		return -1
	else:
		return 0

sort_number_list = [36,25,14,96,42]
print sorted(sort_number_list, reversed_cmp)
print sorted(sort_number_list)
