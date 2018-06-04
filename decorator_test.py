#-*- coding: utf -8-*-

# def log(text):
#     def decorator(func):
#         def wrapper(*args,**kw):
#             print('call %s():'%func.__name__)
#             return func(*args,**kw)
#         return wrapper
#     return decorator

def log(func):
    print('call %s():'%func.__name__)

@log
def now():
    print('2015-3-25')

f=now
f()

print(now.__name__)
print(f.__name__)


