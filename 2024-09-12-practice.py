# Запросіть у користувача ім'я та погодинну ставку в доларах, потім розрахуйте і виведіть їхню тижневу зарплату,
# виходячи з 40-годинного робочого тижня.
# Приклад: "Олексій", "20" → "Тижнева зарплата Олексія становить 800 доларів."
# name = input("Input name: ")
# h_rate = float(input("Input your rate: "))
# h = 40
# result = h * h_rate
# print(f'"{name}", "{h_rate}" → "Тижнева зарплата {name} становить {result} доларів."')


# Попросіть ввести ціле число і виведіть "True", якщо це непарне число в діапазоні від 50 до 150, в іншому випадку виведіть "False".
# user_input = int(input('Input number: '))

# if user_input % 2 == 1 and 50 <= user_input <= 150:
#     print(True)
# else:
#     print(False)
#
# user_input = input('Input number: ')
#
# if user_input.isdigit():
#     user_input = int(user_input)
#     if user_input % 2 == 1 and 50 <= user_input <= 150:
#         print(True)
#     else:
#         print(False)
# else:
#     print('Error')


# Дано ціле число, яке є тризначним числом, де перша цифра не нуль, виведіть число, отримане шляхом реверсу його цифр.
# Приклад: 123 → 321.
# user_input = input('Input numer: ')
# # print(user_input[::-1])
#
# if len(user_input) == 3 and user_input[0] != '0':
#     print(user_input[::-1])
# else:
#     print('Error')
#
# arr = []
# for i in user_input:
#     arr.append(i)
#
# if len(arr) == 3 and arr[0] != '0':
#     arr.reverse()
#     new_number = ''
#     for i in arr:
#         new_number += i #new_number = new_number +i
#     print(new_number)
# else:
#     print('Error')



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

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(f'Max: a = {a}')
# elif b > a:
#     print(f'Max b = {b}')
# else:
#     print(f'Max a and b = {a}')
#
# print(max(a, b))
#
# if a < b:
#     print(f'Max: a = {a}')
# elif b < a:
#     print(f'Min b = {b}')
# else:
#     print(f'Min a and b = {a}')
#
# print(min(a, b))
#
# print(f'Avg: {(a+b)/2}')
# print(f'Sum {a+b}')
# print(f'Sum {sum([a,b])}')
# print(f'Defibition a - b {a-b}')
# print(f'Defibition b - a {b-a}')
# print(f'Defibition |b - a| {abs(b-a)}')
#
# if a == b:
#     print(f'Equal')
# else:
#     print(f'No equal')
#
# print("equal" if a == b else "not equal")




#
# Запросіть у користувача ім'я та кількість годин роботи в тиждень, потім розрахуйте і виведіть їхню місячну зарплату,
# виходячи з фіксованої ставки за годину 15 доларів.
#
# Приклад: "Іван", "40" → "Місячна зарплата Івана становить 2400 доларів."

# name = input("Input name: ")
# h_per_week = float(input("Input your hours: "))
# h_rate = 15
# weeks = 4
# result = h_per_week * h_rate * weeks
# print(f'"{name}", "{h_per_week}" → "Місячна зарплата {name} становить {result} доларів."')
#
#
#
# Запросіть тризначне ціле число і виведіть "True", якщо сума його цифр є простим числом, в іншому випадку виведіть "False".

user_input = input('Input number: ')
if user_input.isdigit() and len(user_input) == 3 and user_input[0] != '0':
    summa = 0
    count = 0
    for i in user_input:
        summa += int(i)

    for i in range(1, summa + 1):
        if summa % i == 0:
            count += 1
    if count == 2:
        print(True)
    else:
        print(False)
else:
    print('Error')

# 10 -> 1, 2, ... 10

# Введіть додатне ціле число як вхідні дані (переконайтеся, що воно знаходиться в межах від 1 до 100),
# розрахуйте і виведіть його факторіал.
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
