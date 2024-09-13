# x = 5
# x += 1 # x = x + 1
# print(x)
# x -= 1
# print(x)
# x *= 2
# print(x)
# x /= 2
# print(x)
# x **= 2
# print(x)
# x //= 2
# print(x)
# x %= 5
# print(x)

# a = True
# b = False
# print(a and b)

# print(True and True)
# print(False and True)
# print(True and False)
# print(False and False)

# print(True or True)
# print(False or True)
# print(True or False)
# print(False or False)

                    # False
# print(True or True and False)

# print(not True)
# print(not False)

# str1 = "Hello"
# print('o' in str1)
# print('o' not in str1)
#
# arr = [1,2,3]
# print(1 in arr)
# print(1 not in arr)
#
# x = "hello"
# y = x
# print(x is y)
# print(y is x)
#
# x1 = "hello"
# y1 = "hello"
# print(x1 is y1)

# str2 = "Hello world"
# str3 = "Hello 'world'"
# print(str2[1])
# print(str2[-1])
# print(str2[0:8:2])
# print(str2[:4])
# print(str2[:-2])
# print(str3[6])

# name = 'username'
# lastname = 'lastname'
# a = 1
# str4 = f'Hello {name} {lastname} {a}'
# print(str4)
# print('%s Hello %s %d' %(name, lastname, a))
# print(f'Hello {name} {lastname} {a}')
#
# print('Hello {1} {0}'.format(name, lastname))
# print('Hello {n} {l}'.format(n=name, l=lastname))
# print('Hello ' + name + ' Hello ' + lastname + ' ' + str(a))

# str5 = '''"Name"
# Info
# '''
# print(str5)
#
# str6 = "Hello \nworld \t Hello"
# print(str6)

# str7 = "Hello world wo"
# print(len(str7))
#
# print(str7.find("wo",0,4))
# print(str7.find("wo"))

# print(str7.index("wo",0,4))

# print(str7[-3:].replace('wo', 'A',1))

str8 = ' Hello, World, Hello '
print(str8[::-1])
print(str8.split(', '))
print(str8.startswith("Hello"))
print(str8.startswith("llo"))
print(str8.endswith("llo"))
print(str8.endswith("ll"))
print(str8.center(50,'*'))
print(str8.ljust(50,'*'))
print(str8.rjust(50,'*'))
print(str8.count('ll'))
print(str8.strip())
