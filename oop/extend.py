# -*- coding: utf-8 -*-
class Animal(object):
	def run(self):
		print 'Animal is running'

class Dog(Animal):
	def run(self):
		print 'Dog is running'

class Cat(Animal):
	def run(self):
		print 'Cat is running'

def twiceRun(Animal):
	Animal.run()
	Animal.run()


print isinstance(Dog(), Animal)
print isinstance(Cat(), Animal)
print isinstance(Animal(), Dog)

twiceRun(Dog())
twiceRun(Cat())