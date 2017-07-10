# -*- coding: utf-8 -*-

print u'对象的定义：'
print u'class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的'
print 'eg:'
print u'参数名必须是object,表示从object继承'
print u'注意到__init__方法的第一个参数永远是self'
class Student(object):
	def __init__(self, name, score):
		self.name = name
		self.score = score

	def print_score(self):
		print 'name:%s, score:%s' % (self.name, self.score)

moben = Student('Moben',99)
meiLin = Student('MeiLin', 100)

moben.print_score()
meiLin.print_score()