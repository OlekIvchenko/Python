# Введіть додатне ціле число як вхідні дані (переконайтеся, що воно знаходиться в межах від 1 до 100),
# розрахуйте і виведіть його факторіал.
# Приклад: 5 → 120.
# number = int(input("Input number: "))
# fact = 1
# if 1 <= number <= 100:
#     for i in range(1, number+1):
#         fact *= i
#     print(f'{number} -> {fact}')
# else:
#     print(f'Error 1 < {number} < 100')

# Запросіть у користувача ім'я та його вік, потім розрахуйте і виведіть рік, в якому він досягне 100 років.
# Приклад: "Емма", "20" → "Емма досягне 100 років у 2100 році."
# name = input('Input your name: ')
# age = int(input('Input your age: '))
# year_now = 2024
# result = year_now - age + 100
# print(f'"{name}", "{age}" → "{name} досягне 100 років у {result} році."')

# Користувач вводить чотиризначне число (переконайтеся, що перша цифра не нуль), і виведіть цифру в тисячному розряді.
# Приклад: 2345 → 2.
# number = input("Input number: ")
# if number.isdigit() and number[0] != '0' and len(number) == 4:
#     print(f'{number} -> {number[0]}')
#     int_number = int(number)
#     result = int_number // 1000
#     print(f'{number} -> {result}')
# else:
#     print('Error')

# До заняття 4: "Immutable ordered collections, unordered collections, Union, intersection, difference and symmetric difference, dictionaries, Collection functions, Functions, zip"
#
#
# Задачі на тему Immutable ordered collections:
# 1. Створіть кортеж (tuple) з елементами "apple", "banana", "cherry". Змініть другий елемент на "grape"
# і виведіть змінений кортеж.
# fruits = ("apple", "banana", "cherry")
# print(fruits)
# fruits = fruits[:1] + ('grape',) + fruits[2:]
# print(fruits)
#
# 2. Порівняйте різні способи створення кортежів за допомогою круглих дужок та функції tuple(). Яка різниця між ними?
# fruits = ("apple", "banana", "cherry")
# fruits1 = tuple(["apple", "banana", "cherry"])
# print(fruits)
# print(fruits1)

# 3. Створіть кортеж з числами від 1 до 5 та використайте зрізи (slicing), щоб вивести перші три елементи.
# numbers = range(1,6)
# print(tuple(numbers)[:3])
#
#
# Задачі на тему Unordered collections:
#
#
#
# 1. Створіть множину (set) з числами 1, 2, 3, 4, 5. Додайте число 6 та виведіть множину.
# numbers = set(range(1,6))
# print(numbers)
# numbers.add(6)
# print(numbers)
#
# # 2. Перевірте, чи є елемент 3 у множині, використовуючи оператор in.
# print(3 in numbers)
# print(7 in numbers)
# 3. Знайдіть перетин двох множин: {1, 2, 3, 4} та {3, 4, 5, 6}.
# numbers1 = {1,2,3,4}
# numbers2 = {3,4,5,6}
# print(numbers1.intersection(numbers2))
# print(numbers1 & numbers2 )
#
#
# Задачі на тему Union, intersection, difference і symmetric difference:
#
#
#
# 1. Об'єднайте множини {1, 2, 3} та {3, 4, 5} та виведіть результат.
#
# number1 = {1,2,3}
# number2 = {3,4,5}
# print(number1.union(number2))
# print(number1 | number2)
# # 2. Знайдіть різницю між множинами {5, 6, 7, 8} та {7, 8, 9, 10}.
# number1 = {5,6,7,8}
# number2 = {7,8,9,10}
# print(number1.difference(number2))
# print(number2.difference(number1))
# print(number1 - number2)
# print(number2 - number1)
# # 3. Визначте симетричну різницю між множинами {1, 2, 3, 4} та {3, 4, 5, 6}.
# numbers1 = {1, 2, 3, 4}
# numbers2 = {3, 4, 5, 6}
# print(numbers1.symmetric_difference(numbers2))
# print(numbers2.symmetric_difference(numbers1))
# print(numbers1 ^ numbers2)
# #
#
# Задачі на тему dictionaries:
#
#
#
# 1. Створіть словник (dictionary) з ключами "name" та "age", де значення ключа "name" - ваше ім'я,
# а значення ключа "age" - ваш вік.
#
# person = {"name": "Alex", "age": 23}
# person1 = dict(name="Alex", age=23, gender = 'W')
# print(person.get('name'))
# print(person['name'])
# print(person1.get('age'))
# person['name'] = [person['name'], 'Oleg']
# print(person)

# 2. Додайте до створеного словника новий ключ "city" зі значенням вашого міста проживання.
#
# person['city'] = 'Dnipro'
# print(person)
# add_person1 = {'city': 'Dnipro'}
# person1['name'] = [person1['name'], add_person1]
# print(person1)
# person1.update(add_person1)
# print(person1)
# 3. Виведіть значення ключа "age" та перевірте, чи існує ключ "gender" у словнику.
# print('gender' in person)
# person.setdefault("gender", 'M')
# person1.setdefault("gender", 'M')
# print(person)
# print(person1)
#
#
# Задачі на тему Collection functions:
#
#
#
# 1. Створіть список чисел від 1 до 10 та знайдіть його суму, максимальне та мінімальне значення.
#
# numbers = list(range(1,11))
# print(numbers)
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))
# 2. Перетворіть список строк ["apple", "banana", "cherry"] в одну строку, розділену комами.
#
# fruits = ["apple", "banana", "cherry"]
# str1 = ",".join(fruits)
# print(str1)
# 3. Перевірте, чи всі елементи списку [True, False, True, True] є істинними.
# #
# list_bool = [True, False, True, True]
# flag = True
# for i in list_bool:
#     # print(i)
#     if i == False:
#         flag = False
#         break
#
# if flag == False:
#     print('Error')
# else:
#     print('All True')
# print(all(list_bool))
#
#
# Задачі на тему Functions:
#
#
#
# 1. Напишіть функцію, яка приймає два аргументи (число та степінь) і повертає результат піднесення числа до степеня.
#
# def power(x:float, y:float):
#     return x**y
# print(power(2,3))
# 2. Напишіть функцію, яка приймає список чисел та повертає список тільки з парних чисел.
#
# def filter_list(arr1:list[float]) -> list:
#     """функцію, яка приймає список чисел та повертає список тільки з парних чисел"""
#     arr2 = []
#     for i in arr1:
#         if i % 2 == 0:
#             arr2.append(i)
#     return arr2
#     return [num for num in arr1 if num % 2 == 0]
# #
# #
# print(filter_list([1,2,3,4,5,6,7,8,9]))
# print(filter_list(list(range(1,100))))
# 3. Напишіть функцію, яка приймає рядок і повертає кількість голосних букв у ньому.
#
# def count_letters(s:str):
#     l = ['a','e','o','u','i']
#     return sum(1 for char in s.lower() if char in l)
# print(count_letters("Hello, world"))
#
#
# Задачі на тему zip:
#
#
#
# 1. Об'єднайте два списки [1, 2, 3] та ['a', 'b', 'c'] за допомогою функції zip() і виведіть результат.
#
# arr1 = [1, 2, 3]
# arr2 = ['a', 'b', 'c']
# print(list(zip(arr1, arr2)))
# 2. За допомогою zip() створіть словник, де ключами будуть елементи списку [1, 2, 3],
# а значеннями - відповідні елементи списку ['one', 'two', 'three'].
#
# arr1 = [1, 2, 3]
# arr2 = ['one', 'two', 'three']
# print(dict(zip(arr1, arr2)))
# # 3. За допомогою zip() та списку індексів створіть список кортежів, де кожен кортеж містить елемент
# # з першого списку та відповідний елемент з другого списку.
# arr1 = [1, 2, 3]
# arr2 = ['one', 'two', 'three']
# print(tuple(zip(arr1, arr2)))
#
#
#
#
#
#
# До заняття 5: "Multi-file programs, Clean code principles, str functions, formatting, time & datetime, optional function arguments, *, operators"
#

#
# Задачі на тему "Clean code principles":
#
#
#
# 1. Перепишіть функцію так, щоб кожен рядок мав ясне призначення та був добре описаний.
#
# 2. Видаліть непотрібні коментарі та зайвий код з вашого проекту, зберігаючи при цьому зрозумілість.
#
# 3. Перегляньте імена змінних та функцій у вашому коді. Перейменуйте їх так, щоб їх назви були інформативними та зрозумілими.
#
#
#
# Задачі на тему "str functions, formatting":
#
#
#
# 1. Напишіть функцію, яка приймає рядок та повертає його довжину, а також кількість голосних та приголосних літер.
# def return_info(s:str) -> tuple:
#     l = 'aeiouy'
#     l1 = 'qwrtpsdfghjklzxcvbnm'
#     return (len(s), sum(1 for char in s.lower() if char in l), sum(1 for char in s.lower() if char in l1))
# lenth, golsni, prigolosni = return_info("Hello world")
# print(lenth)
# print(golsni)
# print(prigolosni)

# 2. Змініть регістр рядка з великих літер на маленькі та навпаки.
#
# print("HELLO".swapcase())
# print("hello".swapcase())
# print("heLLo".swapcase())
# 3. Сформатуйте рядок так, щоб дата була у форматі "dd/mm/yyyy".
# def format_date(day, month, year):
#     return f"{day:02d}/{month:02d}/{year:04d}"
# print(format_date(7,6,24))

#
#
# Задачі на тему "time & datetime":
#
#
#
from datetime import datetime
# 1. Напишіть програму, яка визначає, чи є поточний рік високосним.
#
# def is_leap_year(year):
#     return year % 4 == 0
# print(is_leap_year(datetime.now().year))
# print(is_leap_year(2023))
# 2. Створіть функцію, яка приймає дві дати та повертає різницю між ними в днях.
#
# def days_between(date1, date2):
#     date_format = "%d.%m.%Y"
#     d1 = datetime.strptime(date1, date_format)
#     d2 = datetime.strptime(date2, date_format)
#     return (d2 - d1).days
# print(days_between('01.07.2008', '01.07.2009'))

# 3. Напишіть програму, яка виводить поточну дату та час у форматі "dd/mm/yyyy hh:mm:ss".
#
# def current_date():
#     now = datetime.now()
#     return now.strftime('%d/%m/%Y %H:%M:%S.%f')
# print(current_date())
#



# 1. Напишіть програму для керування шаховим
# турніром: для кожного з 10 раундів, введіть ім’я
# переможця раунду. В кінці роздрукуйте кожен
# учасник, який отримав принаймні один виграш (друкованим шрифтом ім’я та # виграш),
# відсортовано за кількістю перемог у порядку
# спадання.
# def chess():
#     winners = {}
#     for round_num in range(1,6):
#         winner = input(f'Input winner name {round_num}: ').lower()
#         if winner in winners:
#             winners[winner] += 1
#         else:
#             winners[winner] = 1
#     sorted_w = sorted(winners.items(), key = lambda x: x[1], reverse=True)
#
#     return sorted_w
#
# result = chess()
# for name, wins in result:
#     print(f'{name.title()} : {wins}')




# 2. Напишіть програму для відпрацювання мат. операцій. Поки користувач не хочете вийти,
# рандомізуйте оператори (+, -, *) і операнди, і
# перевірити відповідь користувача.Після того, як
# користувач вийде, надрукуйте його бали (у %
# скільки переміг/ скільки всього ігор зіграв)

# Спробуйте написати простий, читабельний код за
# допомогою функцій.


# Create an empty 50x50 grid. Place two points
# on the grid and
# fill a straight line between them on the grid.
# Save the
# resulting grid in three formats:
# 1. As a text file (a “map” of the grid)
# 2. As a JSON file
# 3. As a pickle file
# Compare the resulting files.

import json
import pickle

def create_grid():
    point1 = (10,10)
    point2 = (40,40)
    grid = [['-' for _ in range(50)] for _ in range(50)]
    # print(grid)
    grid[point1[0]][point1[1]] = 'X' # grid[10][10]
    grid[point2[0]][point2[1]] = 'X'
    for i in range(11,40):
        grid[i][i] = 'X'
    return grid

def save_grid(grid):
    with open('grid.txt', 'w') as file:
        for row in grid:
            file.write(''.join(row)+'\n')
    with open('grid.json', 'w') as file:
        for row in grid:
            json.dump(''.join(row)+'\n', file)
    with open('grid.pkl', 'wb') as file:
        for row in grid:
            pickle.dump(''.join(row) + '\n', file)
grid = create_grid()
save_grid(grid)

# res = [['-' for _ in range(10)] for _ in range(5)]
# print(res)
# for r in res:
#     print(r)
# print([['-' for _ in range(10)] for _ in range(10)])

# Напишіть функцію для отримання
# цілочисельного введення від користувача;
# якщо вхідне значення не є цілим, надрукуйте
# відповідне повідомлення та спробуйте ще раз.

# Візьміть як вхідні дані два рядки: список імен
# студентів, розділених символом “,”, і список
# їхніх кінцевих оцінок (цілі числа), розділених
# “,”.
# Надрукуйте імена всіх учнів, чий підсумковий
# бал був на рівні мінімум 90. Для цієї вправи
# використовуйте якомога менше рядків коду.

# Напишіть рекурсивну функцію для піднесення
# числа до степеня
# ціле число, тобто реалізуйте a ** b, де b є
# цілим числом