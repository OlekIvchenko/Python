# import random
#
# def input_names_rates(n:int) -> dict:
#     dict_students = {}
#     while True:
#         name = input()
#         rate = random.randint(50,100)
#         result = random.choice([True, False])
#         dict_students[name] = [rate, result]
#
#     return dict_students # {'Alex' : [71, False], 'Oleg' : [65, True]}
#
#
# def print_students(dict_students:dict):
#     for key, value in dict_students.items(): #{'Alex' : [71, False], 'Oleg' : [65, True]} -> [(Alex, [71,False]), (Oleg, [65, True)])]
#         print(f'{key} - {value[0]} - {value[1]}')
#     pass
#
# def find_min_max_rate(dict_students:dict):
#     passing_scores = [value[0] for name, value in dict_students.items() if value[1]]
#     failing_scores = [value[0] for name, value in dict_students.items() if not value[1]]
#     min_passing_score = min(passing_scores, default=100)
#     max_failing_score = max(failing_scores, default=50)
#
#     return min_passing_score, max_failing_score
#
# def check_professor(min_passing_score, max_failing_score):
#     flag = False
#     if max_failing_score < min_passing_score:
#         flag = True
#     if flag:
#         return True, [max_failing_score+1, min_passing_score]
#     else:
#         return False, []
#
# def main():
#     n = int(input())
#     dStudent = input_names_rates(n)
#     print_students(dStudent)
#     min_rate, max_rate = find_min_max_rate(dStudent)
#     professor, range_rates = check_professor(min_rate, max_rate)
#     if professor:
#         print(f'({range_rates[0]} - {range_rates[1]})')
#     else:
#         print(professor)
#
#
# main()
#


# def get_valid_input(prompt):
#     while True:
#         try:
#             value = int(input(prompt))
#             if value <= 0:
#                 raise ValueError("Введіть позитивне ціле число.")
#             return value
#         except Exception as ex:
#             with open('Errors.txt', 'a') as file:
#                 file.write(str(ex) + '\n')
#
#             # print(f"Error: {e}")
# get_valid_input("input: ")

# class Vehicle():
#     def __init__(self, brand, year):
#         self.brand = brand
#         self.year = year
#
#     def start(self):
#         print(f'{self.brand} start')
#
#     def stop(self):
#         print(f'{self.brand} stop')
#
# class Car(Vehicle):
#     def __init__(self, brand, model, year):
#         super().__init__(brand, year)
#         self.model = model
#
#     def start(self):
#         print(f'{self.brand} {self.model} start')
#
# class Auto(Car):
#     def __init__(self, brand, model, year, something):
#         super().__init__(brand, model, year)
#         self.something = something
#
#
# car1 = Car('Audi', 'Q7', 2023)
# car1.start()
# car1.stop()
#
# a = Auto('Audi', "Q7", 2023,'comment')
# a.start()
# a.stop()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return (self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return (self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return  self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y

    def __ne__(self, other):
        # return self.x != other.x and self.y != other.y
        return not self.__eq__(other)

p1 = Point(10,10)
p2 = Point(10,10)
print(p1 + p2)
print(p1 - p2)
print(p1 == p2)
print(p1 < p2)
print(p1 <= p2)
print(p1 > p2)
print(p1 >= p2)
print(p1 != p2)




