# -*- coding: utf-8 -*-

print u'使用@property'
class Student(object):

	@property
	def score(self):
		return self._score

	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise TypeError('param type error')
		if value > 100 or value < 0:
			raise ValueError('value is too big')
		self._score = value

class Person(object):

	@property
	def birth(self):
		return self._birth

	@birth.setter
	def birth(self, value):
		self._birth = value

	@property
	def age(self):
		return 2017- self._birth

person = Person()
person.birth = 1991
print person.age

s = Student()

s.score = 90

print s.score

s.score = 101
print s.score


