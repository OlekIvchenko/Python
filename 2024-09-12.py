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

# a = 0
# while a <= 1000:
#     if a % 3 == 0:
#         print(a)
#     a += 1

# while True:
#     user_input = input('Input number: ')
#
#     if user_input.isdigit():
#         number = int(user_input)
#         print(f'Your number is {number}')
#         break
#     elif user_input.count('.') == 1:
#         integer_part, dot, decimal_part = user_input.partition('.')
#
#         if integer_part.isdigit() and decimal_part.isdigit():
#             number = float(user_input)
#             print(f'Your numer is {number}')
#             break
#
#     print("Error number not str. Try again!")

# int - 1, 2, 3, 10, 10054, -10, -15
# float - 10.5, 1.5, 1.2, -0.8
# str - 'hello', "hello", "h", 'h', "hello world", '5', "10"
# bool - True, False
# list - [1, 2, 3], ["a", 'b'], [1, "b", True, False, 10.5]



# user_input = input('Input number: ')
# print(isinstance(user_input, str))
# number = eval(user_input)
# print(isinstance(number, int))
# print(isinstance(number, float))
# print(isinstance(number, str))
# print(isinstance(number, bool))


# numbers = [1,2,3]
# for i in numbers:
#     print(f'{i} - {i + 2}')

# new_str = 'Hello world'
# for i in new_str:
#     print(i)

# for i in range(100):
#     print(i)
#
# for i in range(1,100):
#     print(i)

# for i in range(1,100,50):
#     print(i)

# print(list(range(1,100,2)))