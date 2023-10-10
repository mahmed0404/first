# декораторы

# def my_decorator(func):
#     def wrapper():
#         print("то что выходит до функции")
#         func()
#         print("то что выходит после функиции")
#     return wrapper

# @my_decorator
# def hello():
#     print("hello word")
# hello()

# def my_decorator(func):
#     def wrapper():
#         print("то что выходит до функции")
#         print(func())
#         b = func()
#         print(b + 10)
#     return wrapper

# @my_decorator
# def hello():
#     n = 5+5
#     return n
# hello()


# def repeat(num):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#          for _ in range(num):
#             func(*args, **kwargs)
#         return wrapper
#     return decorator

# @repeat(3)
# def say_hello():
#     print('hello')
# say_hello()

# def auth_decor(func):
#     def wrapper(username, password, *args, **kwargs):
#         if username == "admin" and password == "secret":
#             result = func(*args, **kwargs)
#         else:
#             result = 'error'
#         return result
#     return wrapper

# @auth_decor
# def my_func():
#     return 'доступ разрешон'

# print(my_func("admin",'secret'))
 
 
