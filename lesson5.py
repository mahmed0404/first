# цикл while 

# while условия:
#     блок кода будет работать
#     до тех пор пока условия  == true

# n = int(input("число"))
# num = 1

# while num <= n:
#     print(num)
#     num+=1


# password = "qwerty123"
# input_pass = input("введите пороль")
# count = 3
# while input_pass != password:
#     input_pass = input("введите еще раз")
#     count -=1
#     print(f'осталось {count} попыток')
#     if count == 0:
#         print('вы истратили все попытки')
#         break
# print("доступ разрешен")

# while True:
#     answer = input('хотите выйти из цикла? (да\нет)')
#     if answer == "да":
#         break
# print("вы вышли")


# i = 0
# while i < 5:
#     i+=1
#     if i == 3:
#         continue
#     print(i)

# flag = True
 
# while flag:
#     if answer == "да":
#     answer = input('хотите выйти из цикла? (да\нет)')
#        flag = False
# print("понял")




# password = "1234"
# input_pass = input("введите пороль")

# while input_pass != password:
#     input_pass = input("введите еще раз")
# print("доступ разрешен")


# num = 4
# while True:
#     user = int(input('угадай число от 10 до 0'))
#     if user == num:
#         print("угадал")
#         break
#     elif user < num:
#         print("больше")
#     else:
#         print("менеше")
        
        
# n = int(input("вести "))
# fact = 1
# i = 1
# while i <= n:
#     fact *= i
#     i += 1
# print(fact)