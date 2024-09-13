# Запросіть у користувача ім'я та погодинну ставку в доларах, потім розрахуйте і виведіть їхню тижневу зарплату, виходячи з 40-годинного робочого тижня.
#
# Приклад: "Олексій", "20" → "Тижнева зарплата Олексія становить 800 доларів."
#
#
#
# Попросіть ввести ціле число і виведіть "True", якщо це непарне число в діапазоні від 50 до 150, в іншому випадку виведіть "False".
#
#
#
# Дано ціле число, яке є тризначним числом, де перша цифра не нуль, виведіть число, отримане шляхом реверсу його цифр.
#
# Приклад: 123 → 321.
#
#
#
# Запросіть у користувача два цілих числа і виведіть:
#
# a. Максимум із двох чисел
#
# b. Мінімум із двох чисел
#
# c. Середнє значення двох чисел
#
# d. Добуток двох чисел
#
# e. Різницю між двома числами
#
# f. "Рівні", якщо числа однакові, в іншому випадку "Не рівні"
#
#
#
# Запросіть у користувача ім'я та кількість годин роботи в тиждень, потім розрахуйте і виведіть їхню місячну зарплату, виходячи з фіксованої ставки за годину 15 доларів.
#
# Приклад: "Іван", "40" → "Місячна зарплата Івана становить 2400 доларів."
#
#
#
# Запросіть тризначне ціле число і виведіть "True", якщо сума його цифр є простим числом, в іншому випадку виведіть "False".
#
#
#
# Введіть додатне ціле число як вхідні дані (переконайтеся, що воно знаходиться в межах від 1 до 100), розрахуйте і виведіть його факторіал.
#
# Приклад: 5 → 120.
#
#
#
# Запросіть у користувача ім'я та його вік, потім розрахуйте і виведіть рік, в якому він досягне 100 років.
#
# Приклад: "Емма", "20" → "Емма досягне 100 років у 2100 році."
#
#
#
# Користувач вводить чотиризначне число (переконайтеся, що перша цифра не нуль), і виведіть цифру в тисячному розряді.
#
# Приклад: 2345 → 2.

# arr_numb = [1,2,3]
# arr_str = ['Hello', "world"]
# arr = [1,2,3,'Hello',"world", True]
# print(arr_numb)
# print(arr_numb[2])
# print(arr[1:4])
# print(arr[-1])
# arr1 = []
# print(arr1)

# arr2 = [1, 2, [9, 8, [12, 13], 10], 4, 5, 3]
# print(arr2[0])
# print(arr2[1])
# print(arr2[2])
# print(arr2[2][0])
# print(arr2[2][1])
# print(arr2[2][2])
# print(arr2[2][-1])
# print(arr2[2][2][0])
# print(arr2[2][2][-1])
# print(arr2[3])
#
# arr3 = ['Alex', [85,90,70], 'Oleg', [60,55,100]]
# arr4 = [[40000,45000],[35,42],['metro','hospital']]

# arr5 = [1, 2, 3]
# arr5.append(4)
# print(arr5[3])
# print(arr5)
# arr6 = [5, 6]
# arr5.extend(arr6)
# print(arr5)

# arr7 = ["hello", 1, 2]
# arr7.append(1)
# arr7.append("World")
# arr7.append([4,5])
# print(arr7)
#
# arr8 = [1,2,3]
# # arr8.extend('hello')
# arr8.extend([1,"world", [4,5]])
# print(arr8)

# arr9 = [1,2,3]
# arr9.insert(1,5)
# arr9.insert(2,5)
# print(arr9)

# arr10 = [1,2,1, 'hello']
# arr10.remove(1)
# arr10.remove(1)
# print(arr10)

# arr11 = [1,2]
# c = arr11.pop(0)
# print(arr11)
# print(c)

# arr12 = [1,2,1]
# print(arr12.index(1,0,3))
# b = arr12.index(2)
# print(b)
# print(arr12[b])

# arr13 = [1,2,-1,2,3,1,4,5,6,1]
# # count_1 = arr13.count(1)
# # print(count_1)
#
# arr13.sort()
# print(arr13)
#
# arr14 = ['a', "hello",'b','ar','ab','abc']
# arr14.sort()
# print(arr14)

# arr15 = [1,2,3]
# arr16 = arr15.copy()
# arr17 = arr15
# arr15.reverse()
# print(arr15)
# print(arr16)
# print(arr17)
# arr15.clear()
# print(arr15)
# print(arr17)


# age = 15
# name = "Alex"
# if (age == 16 and name == "Alex") or age >= 18:
#     age += 5 # age = age + 5
#     print("Ok")
#     print(age)
# elif age == 17:
#     age *= 2
#     print(age)
# else:
#     pass
    # age -= 5
    # print("No")
    # print(age)

# number = 8
# if number % 2 == 0:
#     print('Even')
# else:
#     print('Odd')

# a = 10
# b = 10
# area = a * b
# if area >= 100:
#     print('Big')
# else:
#     print("Small")



# name_figure = input('Input name of figure: ')
# name_figure_lower = name_figure.lower()
# flag = False
#
# if name_figure_lower == 'rect' or name_figure_lower == "rectangle":
#     a = float(input('Input a: '))
#     b = float(input('Input b: '))
#     if a < 0 or b < 0:
#         pass
#     else:
#         area = a * b
#         flag = True
# elif name_figure_lower == 'circle':
#     r = float(input('Input r: '))
#     if r < 0:
#         pass
#     else:
#         area = 3.14*(r**2)
#         flag = True
# else:
#     print(f"Error {name_figure}")
#
# if flag == True:
#     if area >= 100:
#         print(f"Big area = {area}")
#     else:
#         print("Small")
# else:
#     print("Error Area None")


# a = 0
# while a < 101:
#     if a % 2 == 0:
#         print(f"Even {a}")
#     # elif a == 22:
#     #     a += 1
#     #     continue
#     else:
#         a += 1
#         continue
#         # print(f"Odd {a}")
#     a += 1

a = 0
while a <= 1000:
    if a % 3 == 0:
        print(a)
    a += 1
