#!/usr/bin/env pthon3
# -*- coding: utf-8- -*-

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running...')

def run_twice(animal):
    animal.run()
    animal.run()

class Timer(object):

    def run(self):
        print('Start...')

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
run_twice(Tortoise())
run_twice(Timer())

# dog = Dog()
# cat = Cat()
#
# dog.run()
# cat.run()


