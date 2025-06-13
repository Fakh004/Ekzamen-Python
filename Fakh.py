# 🧠 1. Общая информация о Python

# Что такое Python и какие его основные особенности как языка программирования?
# What is Python and what are its main features as a programming language?
# Пайтон чист ва кадом хусусиятҳои асосӣ ҳамчун забони барномасозӣ дорад?

#Payton - Eto visokourovenniy zaboni programmavii interpretari buda  oson va fahmo sintaksis dorad. Vayro bisyortar dar har guna  veb razrabotki to isskustvennogo intelekta istifoda mebarand 

#------------------------------------------------------------------------------------------------------------------------

# 🧠 2. Типизация в Python
# Какой тип типизации используется в Python? Чем отличается динамическая типизация от статической?
# What type of typing does Python use? What is the difference between dynamic and static typing?
# Дар Python кадом намуди типсозӣ истифода мешавад? Тафовут миёни типсозии динамикӣ ва статикӣ дар чист?

# V pythone Ispolzuetca динамическая типизация yane tipash dar vaqti kor khudash muayan meshavad na in ki misli c++ va Java tipshona khdt menavisi dar статической tipsha khdt menavisi (yane int float string char doubl)

# 🧠 3. Интерпретатор и компилятор
# В чём разница между интерпретатором и компилятором? К какому типу относится Python?
# What is the difference between an interpreter and a compiler? Which one does Python use?
# Фарқи интерпретатор ва компилятор дар чист? Python ба кадом навъ тааллуқ дорад?

#Python ba interpretari dokhil meshavad va farqiyatash dar on hast ki bo tartibi muayan kodro ijro mekunad

#------------------------------------------------------------------------------------------------------------------------

# 1. Сумма двух чисел
# 🔹 RU: Введите два целых числа. Выведите их сумму.
# 🔹 EN: Input two integers. Output their sum.
# 🔹 TJ: Ду адади бутуни ворид кунед. Ҳосили ҷамъро чоп кунед.

# a=int(input())
# b=int(input())
# print(a+b)

# 📌 Пример / Example / Мисол:
# Ввод: 5 3
# Вывод: 8

#------------------------------------------------------------------------------------------------------------------------

# 2. Проверка чётности
# 🔹 RU: Введите число. Если оно чётное, выведите "Even", иначе "Odd".
# 🔹 EN: Input a number. If it is even, print "Even", otherwise print "Odd".
# 🔹 TJ: Як адад ворид кунед. Агар ҷуфт бошад "Even", агар на — "Odd" чоп кунед.

# a=int(input())
# if a%2==0:
#     print('Even')
# elif a%2!=0:
#     print('Odd')

# 📌 Пример:
# Ввод: 7
# Вывод: Odd

#------------------------------------------------------------------------------------------------------------------------

# 3. Повтор строки
# 🔹 RU: Введите строку и число n. Выведите эту строку n раз.
# 🔹 EN: Input a string and a number n. Print the string n times.
# 🔹 TJ: Як сатр ва як адад n ворид кунед. Сатрро n маротиба чоп кунед.

# 📌 Пример:
# Ввод: Hi 3
# Вывод: 
# Hi  
# Hi  
# Hi

# a=input()
# number=int(input())
# for i in range(number):
#     print(a)

#------------------------------------------------------------------------------------------------------------------------

# 4. Максимум из трёх чисел
# 🔹 RU: Введите три числа. Выведите наибольшее из них.
# 🔹 EN: Input three numbers. Print the largest one.
# 🔹 TJ: Се адад ворид кунед. Аз онҳо бузургтаринашро чоп кунед.

# 📌 Пример:
# Ввод: 4 9 2
# Вывод: 9

# import math
# a=int(input())
# b=int(input())
# c=int(input())
# print(max(a,b,c))

#------------------------------------------------------------------------------------------------------------------------

# 5. Количество чётных чисел в списке
# 🔹 RU: Введите n, затем список из n чисел. Выведите количество чётных чисел.
# 🔹 EN: Input n, then a list of n numbers. Output the number of even numbers.
# 🔹 TJ: Аввал n, пас рӯйхати n ададро ворид кунед. Шумораи ададҳои ҷуфтро чоп кунед.

# 📌 Пример:
# Ввод:
# 5  
# 2 7 4 1 8
# Вывод: 3

# a=[]
# n=int(input())
# j=0
# for i in range(n):
#     s = int(input())
#     a.append(s)
# if s%2==0:
#     j+=1
# print(j)

#------------------------------------------------------------------------------------------------------------------------

# 6. Таблица умножения
# 🔹 RU: Введите число. Выведите таблицу умножения от 1 до 10.
# 🔹 EN: Input a number. Print the multiplication table from 1 to 10.
# 🔹 TJ: Як адад ворид кунед. Ҷадвали зарбро аз 1 то 10 чоп кунед.

# 📌 Пример:
# Ввод: 3
# Вывод:

# 3 * 1 = 3  
# 3 * 2 = 6  
# ...  
# 3 * 10 = 30

# a=int(input())
# for i in range(1,11):
#     print(f'{a} * {i} = {a*i}')

#------------------------------------------------------------------------------------------------------------------------


# 7. Сумма чисел до нуля
# 🔹 RU: Вводите числа, пока не введёте 0. Выведите их сумму.
# 🔹 EN: Keep inputting numbers until you enter 0. Print their sum.
# 🔹 TJ: То ворид кардани 0 ададҳо ворид кунед. Ҳосили ҷамъро чоп кунед.

# 📌 Пример:
# Ввод: 4 1 3 0
# Вывод: 8

# sum=0
# while True:
#     n=int(input())
#     sum+=n
#     if n==0:
#         break
# print(sum)

#------------------------------------------------------------------------------------------------------------------------

# 8. День недели (match case)
# 🔹 RU: Введите число от 1 до 7. Выведите день недели. Иначе — "Ошибка".
# 🔹 EN: Input a number from 1 to 7. Print the weekday. Otherwise, print "Error".
# 🔹 TJ: Аз 1 то 7 як адад ворид кунед. Номи рӯзи ҳафтаро чоп кунед. Агар не — "Хато".

# 📌 Пример:
# Ввод: 5
# Вывод: Пятница / Friday / Ҷумъа

# if a==1:
#     print("Yakshanbe")
# elif a==2:
#     print('Dushanbe')
# elif a==3:
#     print('Seshanbe')
# elif a==4:
#     print('Chorshanbe')
# elif a==5:
#     print('Panjshanbe')
# elif a==6:
#     print('Juma')
# elif a==7:
#     print('Shanbe')
# else:
#     print('Khato')

# a=int(input())

# match a:
#     case 1:
#         print('Yakshanbe')
#     case 2:
#         print('Dushane')
#     case 3:
#         print('Chorshanbe')
#     case 4:
#         print('Panjshanbe')

#------------------------------------------------------------------------------------------------------------------------


# 9. Последовательность Фибоначчи
# 🔹 RU: Введите число n. Выведите список из n первых чисел Фибоначчи.
# 🔹 EN: Input a number n. Output a list of the first n Fibonacci numbers.
# 🔹 TJ: Як адад n ворид кунед. Аввалин n адади Фибоначчиро дар рӯйхат чоп кунед.

# 📌 Пример:
# Ввод: 6
# Вывод: [0, 1, 1, 2, 3, 5]

# n=int(input())
# fib=[]
# for i in range(n):
#     if i==0:
#         fib.append(0)
#     elif i==1:
#         fib.append(1)
#     else:
#         fib.append(fib[i-1] + fib[i-2])
# print(fib)



# 10.Task
# 📌 Условие (RU):
# Введите список чисел. Разделите его на два новых списка:
# – все числа с чётным индексом,
# – все числа с нечётным индексом.
# Выведите их отдельно.

# 📌 Условие (EN):
# Input a list of numbers. Split it into two new lists:
# – numbers with even indexes,
# – numbers with odd indexes.
# Print both lists.

# 📌 Условие (TJ):
# Рӯйхати ададҳоро ворид кунед. Онро ба ду рӯйхат ҷудо кунед:
# – индексҳои ҷуфт,
# – индексҳои тоқ.
# Ҳарду рӯйхатро чоп кунед.

# Пример:

# python
# Копировать
# Редактировать
# # Ввод: [5, 8, 1, 4, 9, 2]
# # Чётные индексы (0,2,4): [5, 1, 9]
# # Нечётные индексы (1,3,5): [8, 4, 2]
# # Вывод:
# # [5, 1, 9]
# # [8, 4, 2]

# a=[]
# n=int(input())
# for i in range(n,a):
#     if i%a==0:
#         print(i)