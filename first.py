# onesa = 2.5
# twoesa = 2
# dic = onesa * twoesa
# print(dic)
# print(type(dic))

# name = str(input("Please input your name" ))
# domain = str(input("Please input your domain" ))
# print(name, domain, sep= "@")

# print(my, name, is, Olecsandr, sep= "**")

# var = 4.5
# var = int(var)
# print(type(var))
# print(var)
# print("""this
# is a
# multiline
# text""")   
# if type(age) is int:
# i
# num = int(input("Enter the integer (0 to 100): "))
# sum = 0
# i = 1
# while 0 < i <= num:
#     sum += i
#     i = i + 1
# print(sum)
# message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
# search = "r"
# result = {search: message.count(letter) for search in (message)}
# print(result)
# people = ["qwe", "qwer", "qwert"]
# message = input("Введите сообщение: ")
# offset = int(input("Введите сдвиг: "))
# encoded_message = ""
# cripted = ""
# for ch in message:
#     if ch in "abcdefghijklmnopqrstuvwxyz":
#         pos = ord(ch) - ord("a")
#         pos = (pos + offset) % 26
#         encoded_message = chr(pos + ord("a"))
#         cripted += encoded_message
#     elif ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#         pos = ord(ch) - ord("A")
#         pos = (pos + offset) % 26
#         encoded_message = chr(pos + ord("A"))
#         cripted += encoded_message
#     elif ch == " " or ch == "!":
#         encoded_message = " " or "!"
# print(cripted)


# from re import A


# result = None
# operand = None
# operator = None
# wait_for_number = True
# while True:
#     # Перший блок
#     user_input = input(">>> ")  # достатьно одного інпуту в циклі
#     if user_input == "=":
#         print(result)
#         break
#     # Другий блок
#     if wait_for_number:
#         try:
#             operand = float(user_input)  # тут присвоюємо user_input до операнда
#             wait_for_number = False
#         except ValueError:
#             print("is not a number")
#             continue
#         if result is None:
#             result = operand
#         if operator == "+": # тут блок математичних операцій, якщо оператор + то ми до результуту додаємо операнд
#             result += operand
#         elif operator == "-":
#             result -= operand
#         elif operator == "*":
#             result *= operand
#         elif operator == "/":
#             result /= operand
#     # Третій блок
#     else:
#         if user_input in "+-*/":
#             operator = user_input   # тут присвоюємо user_input до змінної operator
#             wait_for_number = True
#         else:
#             print(f'{user_input} is not a operator')
#             continue
# def greeting(name):
#     print(F"hello {name}")

# greeting("Roman")
# x = 50

# def func():
#     x = 2
#     print('Зміна локального x на', x)  # Зміна локального x на 2

# func()
# print('x як і раніше', x)   # x як і раніше 50
# x = 50

# def func():
#     global x
#     print('x дорівнює', x) # x дорівнює 50
#     x = 2
#     print('Змінюємо глобальне значення x на', x)   # Змінюємо глобальне значення x на 2

# func()
# print('Значення x складає', x)   # Значення x складає 2
# base_rate = 40
# price_per_km = 10
# total_trip = 0

# def trip_price(path):
#     sum = price_per_km * path + base_rate 
#     global total_trip
#     total_trip += 1
#     print(sum)
#     return
 
# trip_price(4.3)

# from dis import disco


# def cost_delivery(quantity, *list_of_goods, discount = 0):
#     coast = 0
#     if quantity == 1:
#         coast = 5 
#     else:
#         quantity -= 1
#         coast = quantity * 2 + 5 
#     if discount > 0:
#         coast = coast * discount  
#     return coast
# print(cost_delivery(2, 1, 2, 3, discount=0.5))

# def factorial(n):
#     if n < 2:
#         return 1
#     else:
#         return n * factorial(n - 1)
# def number_of_groups(n, k):
#     Cnk = factorial(n) // (factorial(n - k) * factorial(k))
#     return Cnk    

# print(number_of_groups(100,7))



# 

# fruits = ("apple", "cherry", "banana", "kiwi", "lemon", "pear", "peach", "avocado")
# print(type(fruits))
# print(fruits)
# qwe123 = list(fruits)
# print(type(qwe123))
# print(qwe123)

