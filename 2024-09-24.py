# Задачі на заняття 7: File input / output, JSON, pickle, Serializing and de-serializing Python objects, Easy filtering of collections, map, recursion
#
#
# Задачі на тему "File input/output":
#
#
#
# 1. Напишіть програму, яка створює новий текстовий файл та записує в нього деякий текст.
#
# 2. Реалізуйте функцію, яка зчитує вміст текстового файлу та виводить його на екран.
#
# def create_or_read_file(file_name, w_or_r, text=''):
#     with open(file_name, w_or_r) as file:
#         if w_or_r == 'w':
#             file.write(text)
#             return 0
#         elif w_or_r == 'r':
#             info = file.read()
#             # print(info)
#             return info
#         else:
#             return  (f'Error w_or_r != {w_or_r}')
#
# a = create_or_read_file('new.txt', 'w', 'Information')
# # print(a)
# a = create_or_read_file('new.txt', 'r')
# print(a)
# a = create_or_read_file('new.txt', 'a')
# print(a)
# 3. Напишіть скрипт, який копіює вміст одного файлу в інший.

# def copy_file(file_name1, file_name2):
#     try:
#         with open(file_name1, 'r') as file:
#             info = file.read()
#         with open(file_name2, 'w') as file1:
#             file1.write(info)
#     except FileNotFoundError as ex:
#         print(ex)
#     except Exception as ex:
#         print(ex)
#         return ex
#     return 0
#
# copy_file('new.txt', 'new1.txt')
#
#
# Задачі на тему "JSON":
#
#
#
# 1. Створіть словник та збережіть його у файл у форматі JSON.
#
# 2. Напишіть програму, яка зчитує JSON-файл та виводить його вміст на екран.
#
# 3. Реалізуйте функцію, яка приймає словник та зберігає його у файлі JSON.
# import json
#
# def create_or_read_json(file_name, w_or_r, data={}):
#     with open(file_name, w_or_r) as file:
#         if w_or_r == 'w':
#             json.dump(data, file)
#             return 0
#         elif w_or_r == 'r':
#             info = json.load(file)
#             # print(info)
#             return info
#         else:
#             return  (f'Error w_or_r != {w_or_r}')
# data = {'name': 'Alex', "age" : 30}
# # create_or_read_json('info.json', 'w', data)
# info = create_or_read_json('info.json', 'r')
# print(create_or_read_json('info.json', 'r'))
# print(info)
# print(create_or_read_json('info.json', 'a'))

#
#
# Задачі на тему "pickle":
#
#
#
# 1. Збережіть список або словник у файл за допомогою модулю pickle.
# import pickle
# arr = [1,2,3,4,5]
# with open('arr.pkl', 'wb') as file:
#     pickle.dump(arr, file)
# # # 2. Реалізуйте функцію, яка зчитує об'єкт з файлу pickle та повертає його.
# with open('arr.pkl', 'rb') as file:
#     info = pickle.load(file)
# print(info)
# 3. Напишіть програму, яка використовує модуль pickle для збереження та відновлення об'єктів Python.
#
#
#
# Задачі на тему "Serializing and de-serializing Python objects":
#
#
#
# 1. Створіть клас у Python та збережіть його у файл за допомогою pickle.
# import pickle
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# person1 = Person("Alex", 30)
# with open('person.pkl', 'wb') as file:
#     pickle.dump(person1,file)
# # 2. Реалізуйте функцію, яка десеріалізує об'єкт з файлу та повертає його.
# with open('person.pkl', 'rb') as file:
#     info = pickle.load(file)
# print(info.age)

# 3. Напишіть програму, яка серіалізує об'єкт Python та зберігає його у файлі.
#
#
#
# Задачі на тему "Easy filtering of collections":
#
#
#
# 1. Напишіть функцію, яка фільтрує список чисел за певною умовою (наприклад, лише парні числа).
# nums = [1,2,3,4,5]
# def filter_nums(nums):
#     return list(filter(lambda x: x % 2 == 0, nums))
# print(filter_nums(nums))
# 2. Створіть програму, яка відфільтровує словник за значенням ключа.
# d = {'a': 1, 'b' : 2, 'c' : 3, 'd' : 4}
# arr = ['a', 'c']
# def filter_d(d, arr):
#     return dict(filter(lambda item: item[0] in arr, d.items()))
# print(filter_d(d,arr))
# 3. Реалізуйте функцію, яка відфільтровує список рядків за певною умовою (наприклад, довжиною рядка).
# arr_str = ['a', 'abc', 'abf', 'av']
# def filter_arr_str(arr, len_str):
#     return list(filter(lambda l: len(l) == len_str, arr))
#
# print(filter_arr_str(arr_str, 3))


#
# Задачі на тему "map":
#
#
#
# 1. Напишіть функцію, яка використовує map для подвоєння кожного елементу списку чисел.
#
# nums = [1,2,3,4,5]
# def double_num(arr):
#     return list(map(lambda x: x * 2, arr))
# print(double_num(nums))
# 2. Створіть програму, яка використовує map для перетворення рядків списку у нижній регістр.
# arr_str = ["ABCC", "aBsaA"]
# def arr_lower(arr):
#     return list(map(lambda s: s.lower(), arr))
# print(arr_lower(arr_str))
# 3. Реалізуйте функцію, яка використовує map для обчислення квадратів чисел у списку.
# nums = [1,2,3,4,5]
# def double_num(arr):
#     return list(map(lambda x: x ** 2, arr))
# print(double_num(nums))
#
#
# Задачі на тему "recursion":
#
#
#
# 1. Напишіть рекурсивну функцію для обчислення факторіалу числа.
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return  n * factorial(n-1)
# print(factorial(10))
# n! = 1 * 2 * 3 ... n
# 3! = 1 * 2 * 3 -> 3 * 2!
# 2! = 1 * 2 -> 2 * 1!
# 1! = 1 -> 1 * 0!
# 0! = 1

# 2. Створіть рекурсивну функцію для обчислення суми елементів списку.
# def sum_list(arr):
#     if not arr:
#         return 0
#     else:
#         return arr[0] + sum_list(arr[1:])
# print(sum_list([1,2,3,4,5]))
# [1,2,3,4,5] -> 1 + [2,3,4,5] -> 1 step
# [2,3,4,5] -> 2 + [3,4,5] -> 2 step
# [3,4,5] -> 3 + [4,5] -> 3 step
# [4,5] -> 4 + [5] -> 4 step
# [5] -> 5 + [] -> 5 step
# [] -> 0
# 3*. Реалізуйте рекурсивну функцію для обчислення чисел Фібоначчі.
# 0,1,1,2,3,5,8,13,21...
# def fibonachi(n):
#     try:
#         if n < 0:
#             return f'{n} < 0'
#         elif (n == 1) or (n == 0):
#             return n
#         else:
#             return fibonachi(n-1) + fibonachi(n-2)
#     except Exception as ex:
#         print(ex)
#         return -1
#
# n = 10
# print(fibonachi('ad'))
# for i in range(n+1):
#     print(fibonachi(i))
# 5 -> 1 step -> F(4) + F(3) -> 3 + 2 = 5
# F(4) -> F(3) + F(2) -> 2 + 1 = 3
# F(3) -> F(2) + F(1) -> 1 + 1 = 2
# F(2) -> F(1) + F(0) -> 1 + 0 = 1
# F(1) -> 1
# F(0) -> 0
#
# Задачі на тему 8: Python classes, collection utilities, advanced iteration utilities, Algorithms
#
#
# Задачі на тему "Python classes":
#
#
#
# 1. Створіть клас "Книга" з атрибутами "назва", "автор" і "рік видання". Напишіть метод для виведення інформації про книгу.
#
# 2. Реалізуйте клас "Калькулятор" з методами для додавання, віднімання, множення та ділення чисел.
#
# 3. Створіть клас "Автомобіль" з атрибутами "марка", "модель", "рік випуску" та методом для обчислення кількості років, які пройшли з моменту випуску.
from datetime import datetime
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def count_year(self):
        return f'{self.brand} {self.model} - {datetime.now().year - self.year} year'
car1 = Car('Audi', 'Q7', 2012)
print(car1.count_year())

#
#
# Задачі на тему "collection utilities":
#
#
#
# 1. Напишіть функцію, яка приймає список чисел і повертає список, в якому всі числа більше заданого числа.
#
# 2. Реалізуйте функцію, яка об'єднує два словники в один.
#
# 3. Напишіть програму, яка приймає список слів і повертає словник, де ключами є слова, а значеннями - кількість їх зустрічань у списку.
#
#
#
# Задачі на тему "advanced iteration utilities":
#
#
#
# 1. Напишіть функцію, яка приймає список чисел і повертає суму квадратів непарних чисел.
#
# 2*. Реалізуйте генератор, який видає послідовність простих чисел.
#
# 3. Напишіть функцію, яка приймає список слів і повертає список, в якому всі слова записані в оберненому порядку.
#
#
#
# Задачі на тему "Algorithms":
#
#
#
# 1. Напишіть функцію для сортування списку чисел методом бульбашки.
#
# 2. Реалізуйте алгоритм пошуку максимального підрядка чисел у списку.
#
# 3. Напишіть функцію, яка перевіряє, чи є дане число простим.