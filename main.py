# print("Hello world")
# print('Hello world')
# print('Hello "world"')
# print("Hello 'world'")
# a = 5
# print(a)
# print(type(a))
# b = 5.5
# print(b)
# print(type(b))
# c = '5a'
# print(c)
# print(type(c))
# d = a + b
# print(d)
# print(type(d))
# print(a+b)
# print(c*a)
#
# str1 = '5'
# my_int_var = int(str1)
# print(my_int_var)
# print(type(my_int_var))


# age = int(input("Input Age: "))
# print(type(age))

# print(5+5)
# print(5-5)
# print(5*5)
# print(5/5)
# print(5//2)
# print(9%5)
print(5**3)

h_per_day = 24
m_per_h = 60
s_per_m = 60

result_task_3 = h_per_day * m_per_h * s_per_m
print("Task 3: ", result_task_3, "seconds")

days_per_year = 365
# result_task_4 = h_per_day * m_per_h * s_per_m * days_per_year
result_task_4 = result_task_3 * days_per_year
print("Task 4: ", result_task_4, "seconds")

new_planet = input("Input name new planet ")
second_in_year_new_planet = result_task_4 * 532 / days_per_year
print("In year", new_planet, second_in_year_new_planet, "seconds")

# new_planet = input("Input name new planet ")
# second_in_year_new_planet = result_task_3 * 532
# print("In year", new_planet, second_in_year_new_planet, "seconds")

age_person_month = int(input("Age in month: "))
age_person = age_person_month // 12
print(age_person)
print(age_person > 18)

# print('hello "OOO"')
# print("hello 'OOO'")