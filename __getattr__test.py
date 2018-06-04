#!/usr/bin/env pthon3
# -*- coding: utf-8- -*-


class Student(object):

    def __init__(self):
        self.name = 'Luo'

    # def __getattr__(self, attr):
    #     if attr == 'score':
    #         return 99

    def __getattr__(self, attr):
        if attr == 'age':
            return lambda :25

s = Student()
# print(s.name)
# print(s.score)
print(s.age())

