# -*- coding: utf-8 -*-
class Student(object):
	def __init__(self, name, score):
		self.__name = name
		self.__score = score

	def printScore(self):
		print '%s : %s' % (self.__name, self.__score)

	def get_name(self):
		return self.__name

moben = Student('moben', 99)

moben.printScore()
print moben.get_name()