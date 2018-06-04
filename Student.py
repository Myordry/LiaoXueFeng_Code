#!/usr/bin/env pthon3
# -*- coding: utf-8- -*-

class Student(object):

    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s:%s'%(self.name,self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


bart = Student('Luo',89)
lisa = Student('Xiao',90)
bart.print_score()
lisa.print_score()
print(bart.get_grade())
print(lisa.get_grade())