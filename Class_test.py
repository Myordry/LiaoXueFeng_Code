#!/usr/bin/env pthon3
# -*- coding: utf-8- -*-

class Student(object):

    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def set_score(self,score):
        self.__score = score

    def set_name(self,name):
        self.__name = name

    def get_score(self):
        return self.__score

    def get_name(self):
        return self.__name


    def print_score(self):
        print('%s:%s'%(self.__name,self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'


bart = Student('Luo',89)
lisa = Student('Xiao',90)
jone = Student('Ming',34)

print(bart.get_name())
print(lisa.get_name())
print(jone.get_name())

print(bart.get_score())
print(lisa.get_score())
print(jone.get_score())

bart.print_score()
lisa.print_score()
jone.print_score()

print(bart.get_grade())
print(lisa.get_grade())
print(jone.get_grade())


