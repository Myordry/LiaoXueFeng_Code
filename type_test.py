#!/usr/bin/env pthon3
# -*- coding: utf-8- -*-

# class Hello(object):
#     def hello(self,name = 'world'):
#         print('Hello,%s'% name)

def fn(self,name = 'world'): #先定义函数
    print('Hello,%s'% name)

Hello = type('Hello',(object,),dict(hello = fn)) #创建Hello class

h = Hello()
h.hello()

print(type(Hello))
print(type(h))