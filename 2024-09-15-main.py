# import xtr1
#
# a = 5
# b = 4
# print(xtr1.summa(a, b))
# c = xtr1.summa(a, b)
# print(c)
# print(xtr1.mult(a, b))

# from xtr1 import summa, mult
# a = 5
# b = 4
# print(summa(a, b))
# print(mult(a,b))

# def mult(a, b):
#     return a * b
#
# print(mult(5,5))

from xtr1 import mult, summa, new_summa, new_summa_arr, number, factorial
# print(number)
# print(mult(4,6))
# # print(summa(4))
# c = new_summa(1,2,3,4,5)
# print(c)
# print(new_summa(1,2,3,4,5))
# x = lambda a, b: a if a < b else b
# print(x(4,3))
# print(new_summa_arr([1,2,3,4,5]))

# print(factorial(4))

# x = [4,6,8,9,7,3,4,5,67]
# print(sorted(x))
# print(sorted(x, reverse=True))
# y = [(10,5,89), (6,8,101), (5,9,7)]
# print(sorted(y, key=lambda a: a[0]))
# print(sorted(y, key=lambda a: a[1]))
# print(sorted(y, key=lambda a: a[2]))

a = [1,2,'',3]
b = ['a', 'b','' ,[4,5]]
d = [4,5,6,7]
c = list(zip(a,b,d))
print(c)