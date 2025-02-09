#!/usr/bin/python3
'''
Using abstract classes per fist time
'''


from abc import ABC, abstractmethod


class Animal(ABC):
    '''
    What do the animals do?
    '''
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    '''
    This is a dog
    '''
    def sound(self):
        return "Bark"

class Cat(Animal):
    '''
    This is a cat
    '''
    def sound(self):
        return "Meow"