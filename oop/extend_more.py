# -*- coding: utf-8 -*-
class Animal(object):
	pass

class Runable(Animal):
	pass

class Flyable(Animal):
	pass

class Mammal(Animal):
	pass

class Dog(Mammal, Runable):
	pass

class Cat(Mammal, Runable):
	pass

print u'通过多重继承，一个子类就可以同时获得多个父类的所有功能'
print u'这种设计通常称为Mixin'