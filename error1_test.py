#!/usr/bin/env pthon3
# -*- coding: utf-8- -*-


# try:
#     print('try...')
#     # r = 10 / 2
#     r = 10 / int('2')
#     print('result:',r)
# except ValueError as e:
#     print('ValueError:',e)
# except ZeroDivisionError as e:
#     print('except:',e)
# else:
#     print('no error!')
# finally:
#     print('finally...')
# print('END')



# def foo(s):
#     return 10 / int(s)
#
# def bar(s):
#     return foo(s)*2
#
# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         print('Error:',e)
#     finally:
#         print('finally...')
#
# main()

# # err.py:
# def foo(s):
#     return 10 / int(s)
#
# def bar(s):
#     return foo(s) * 2
#
# def main():
#     bar('0')
#
# main()

#记录错误
# err_logging.py

# import logging
#
# def foo(s):
#     return 10 / int(s)
#
# def bar(s):
#     return foo(s)*2
#
# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         logging.exception(e)
#
# main()
# print('END')

#抛出错误
#err_raise.py
# class FooError(ValueError):
#     pass
#
# def foo(s):
#     n = int(s)
#     if n == 0:
#         raise FooError('invalid value:%s'%s)
#     return 10 / n
#
# foo('0')

#err_reraise.py

def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value:%s'% s)
    return 10 / n
def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError')
        raise 

bar()