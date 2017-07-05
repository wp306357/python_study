# -*- coding: utf-8 -*-
print "hello python!"
print "python-->", "print some word!"
print "200 + 300 =",200+300
print "please input you name:"
#name=raw_input()
#print "my name is","'",name,"'"

a = 100
if a >= 0:
	print a
else:
	print -a

print u'测试中文输出'

#print 'Hi %s, you have %d' % (name,100)

#print u'你好冒险者，我是穆，请问你是'
#name=raw_input(u'请输入姓名:'.encode('gbk')).decode('gbk')
#print u'%s你好，真是一个不错的名字，欢迎来到%s'%(name,u"法兰城")

age = 12
if age>=18:
	print 'you age is', age
	print 'adult'
elif age > 6:
	print 'you age is', age
	print 'teenager'
else:
	print 'kid'
	
sum = 0
for num in range(101):
	sum = sum + num
print sum

#print 'please enter your birth'
#birth = int(raw_input())
#if birth >= 2000:
#	print u'00后'
#else:
#	print u'00前'
	
#测试死循环
#while True:
	#print u'死循环'

def my_abs(x):
		if not isinstance(x,(int,float)):
			raise TypeError('bad param type')
		if x >=0:
			return x
		else:
			return -x
print u'请输入数据'
enter = raw_input()
my_abs(enter)
print u'输入数据绝对值为: %d' % (my_abs(int(enter)))

