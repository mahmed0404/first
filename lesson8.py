# исключения 

# try:
#     num = int(input("ведите  число: "))
#     res = 10 / num
#     print(res)
# except (ValueError,ZeroDivisionError):
#     print("ошибка")
# # except ValueError:
# #     print("ошибка значения")
# # except ZeroDivisionError:
# #     print("тебе же сказали балда не дели на ноль")

# print('ok')
# try:
#     num = int(input("ведите  число2: "))
#     res = 10 / num
#     print(res)
# except ValueError as ve:
#     print("ошибка  {0}".format(ve))
# except ZeroDivisionError:
#     print('ошибка деления на ноль')
# finally:
#     print("ну вот балда правильно")


# try
# except ValueError as ve:
#     print("ошибка  {0}".format(ve))
# except ZeroDivisionError:
#     print('ошибка деления на ноль')
# finally:
#     print("ну вот балда правильно")


# while True:
#     a = float(input("Ведите первое число"))
#     b = str(input("Ведите операция '/' '*' '-' '+' '%' '//'"))
#     c = float(input("Ведите первое число"))
#     car = a ** c
#     if  b == "+":
#         print(a + c)
#     elif b == "-":
#         print(a - c)
#     elif b == "*":
#         print(a * c)
#     elif b == "/":
#         print(a / c)
#     elif b == "%":
#         print(a % c)
#     elif b == "//":
#         print(a // c)
#     else:
#         print("eroor")
#         break
# print("")


# word = str(input(":"))

# resul = word.split()
# resev = reversed(word)
# sel = "".join(resev)
# print(sel)

# user = int(input("ведиет число"))
# if user%2 ==0:
#     print("четное")
# else:
#     print("не четное")



# def cesar(text,shift):
#     result = ""
#     alphaber_lower = 'abcdefghijkoln'
#     for i in text:
#         is_upper = str(i).upper
#         if str(i).isalpha():
#             i_index = alphaber_lower.index(i)
#             i_shift = alphaber_lower[(i_index + shift)] % 26
#             result +=i_shift 
#         else:
#             result += i
        
        
               
# while True:
#     user1 = float(input("ведите первое число"))          
#     user2 = str(input("ведите операцию (/, *, -, +, )"))  
#     user3 = float(input("ведите второе число"))     
#     if user2 == "+":
#         print(user1 + user3)
#     elif user2 == "-":
#         print(user1 - user3)
#     elif user2 == "/":
#         print(user1 / user3)
#     elif user2 == "*":
#         print(user1 * user3)
#     else:
#         print("error")
#         break
# print("")


# alfavit_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghikjlmnopqrstuvwxyz'

# alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхчшщъыьэюя'

# lang = input('Выберите язык RU/EU: ').upper

# smeshnie = int(input('Шаг шифровки: '))

# message = input ('Сообщение для шифровки: ')

# itog = ' '

# if lang == 'RU':
#     for i in message:
#          mesto = alfavit_RU.find(i)
#          new_mesto = mesto + smeshnie
#          if i in alfavit_RU:
#               itog += alfavit_RU[new_mesto]
#          else:
#                 itog += i
# else:
#        for i in message:
#              mesto = alfavit_EU.find(i)
#              new_mesto = mesto + smeshnie
#              if i in alfavit_EU:
#                  itog += alfavit_EU[new_mesto]
#              else:
#                     itog += i
# print(itog)