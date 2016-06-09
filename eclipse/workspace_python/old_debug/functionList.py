from abc import ABCMeta, abstractmethod

class Animal:
    __metaclass__ = ABCMeta

    
    @abstractmethod
    def say_something(self): pass

class Cat(Animal):
    __init__(self, nome):
        self.nome = nome
    
    def say_something(self):
        return "Miauuu!"

cat = Cat('gato 1')
print cat.say_something()


