# built in functions
#  - id, type, len, eval, int, float, input, print


# operators

# - Arithmetic
# - relational coparison --< ><=>= 
# - special operators 
#     - membership -- in, not in
#     - identyty -- is, is not
# - logical -- and, or, not
# -assignment
# - bitwise operator


# Type Conversion

# """
# >>> 2+2
# 4
# >>> "abcd" * 2
# 'abcdabcd'
# >>> "a" + "b"
# 'ab'
# >>> "py" + "thon"
# 'python'
# >>> 12/2
# 6.0
# >>> 12/4
# 3.0
# >>> 12//5
# 2
# >>> 10/6
# 1.6666666666666667
# >>> 10//6
# 1
# >>> 10 % 2
# 0
# >>> 11 % 2
# 1
# >>> 2**2
# 4
# >>> 2**5
# 32
# >>> a = "abcd xyz pqr"
# >>> s1 = "abcd xyz pqr"
# >>>
# >>> "a" in s1
# True
# >>> "abc" in s1
# True
# >>> "abc " in s1
# False
# >>> " " in s1
# True
# >>> "ghi" in s1
# False
# >>> "ghi" not in s1
# True
# >>> l1 = [10,20,30,40]
# >>> 10 in l1
# True
# >>> "30" in l1
# False
# d ={1:1, 2:4, 3:9, 4:16, 5:25}
# 1 in d
# >>> 1 in d
# True
# >>> 4 in d
# True
# >>> 9 in d
# False
# >>> 1 in d
# True
# >>> 8 in d
# False
# >>>
# >>> a = "abcd"
# >>> b = "abcd"
# >>> id(a)
# 1514847805104
# >>> id(b)
# 1514847805104
# >>> c = "abcd"
# >>> id(c)
# 1514847805104
# >>> a is b
# True
# >>> a is not b
# False
# >>> a = [1,2,3,4]
# >>> b = [1,2,3,4]
# >>> id(a), id(b)
# (1514847498304, 1514847499328)
# >>> c = a
# >>> id(c)
# 1514847498304
# >>> a[0] = 10
# >>> a
# [10, 2, 3, 4]
# >>> b
# [1, 2, 3, 4]
# >>> c
# [10, 2, 3, 4]
# >>> c
# [10, 2, 3, 4]
# >>> c[0] = 100
# >>> a
# [100, 2, 3, 4]
# >>> c
# [100, 2, 3, 4]
# >>> z = b
# >>> id(z)
# 1514847499328
# >>> id(b)
# 1514847499328
# >>>   a
#   File "<stdin>", line 1
#     a
# IndentationError: unexpected indent
# >>> a
# [100, 2, 3, 4]
# >>> b
# [1, 2, 3, 4]
# >>> a = [1,2,3,4]
# >>> b = [1,2,3,4]
# >>> a
# [1, 2, 3, 4]
# >>> b
# [1, 2, 3, 4]
# >>> a is b
# False
# >>> a == b
# True
# >>> a is b
# False
# >>> a is not b
# True
# >>> a !=b
# False
# >>> a = "10"
# >>> type(a)
# <class 'str'>
# >>> b =int("10")
# >>> type(b)
# <class 'int'>
# >>> b = int("ab")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: invalid literal for int() with base 10: 'ab'
# >>> int(10)
# 10
# >>> int(10.50)
# 10
# >>> int(10.51)
# 10
# >>> int(10.99)
# 10
# >>> int("10.99")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: invalid literal for int() with base 10: '10.99'
# >>> int("10")
# 10
# >>> int("10.001")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: invalid literal for int() with base 10: '10.001'
# >>> l = 10
# >>> type(l)
# <class 'int'>
# >>> s = str(l)
# >>> s
# '10'
# >>> type(s)
# <class 'str'>
# >>> list("abcd")
# ['a', 'b', 'c', 'd']
# >>> list("abcd123,32")
# ['a', 'b', 'c', 'd', '1', '2', '3', ',', '3', '2']
# >>> complex(10)
# (10+0j)
# >>> complex(10, 2)
# (10+2j)
# >>> l = [10,20,30]
# tuple(l)
# (10, 20, 30)
# >>> l
# [10, 20, 30]
# >>> t = tuple(l)
# >>> type(t)
# <class 'tuple'>
# >>> t[0] = 1000
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment>>> bool(None)
# False
# >>> bool(0)
# False
# >>> bool(1)
# True
# >>> bool(0.000001)
# True
# >>> bool(0+0j)
# False
# >>> bool(0+1j)
# True
# >>> bool([])
# False
# >>> bool(["a", "b"])
# True
# >>> bool(["a"])
# True
# >>> bool([""])
# True
# >>> bool([])
# False
# >>> bool([     ])
# False
# bool([None, False])
# True
# >>> bool(())
# False
# >>> bool((0,))
# True
# >>> bool({})
# False
# >>> bool(False)
# False
# >>> bool(1)
# True
# >> set()
# set()
# >> tuple()
# ()
# >>> dict()
# {}
# >>> []
# []
# >>> list()
# []
# >>> ()
# ()


# Truth Table

# and
# 1 1  1
# 0 1  0
# 1 0  0
# 0 0  o

# or
# 1 1  1
# 0 1  1
# 1 0  1
# 0 0  0

# not
# 1   0
# 0   1


#  concatenation -- 

# floor --
# modulo --
# power/exponant -



# star -- asterisk

# a = 10
# b = 20

# print(a <= b) # less than or equal to

# Equality operator
#  - == , !=


# list aliasing --

# and, or not

# a = 10
# b = 20
# c = 30
# z = 100

# if a + b == c and a**2 == z and type(a) == int: # if true and true and true
#    print("valid")     # indentation -- 4 spaces -- PEP8 Rule
# else:
#     print("Invalid")


# ternary operator

# a, b = 10, 20
# value = "Large" if a > b else "less"
# print(value)

# a, b, c = 10, 20, 30
# minimum = a if a < b and a < c else b if b < a and  b < c else c
# print(minimum)

# Operator precedence --

# module --- built in module --

# math, 

# constat -- 

# LANGAUGE = "Python"


# import math

# print(math.pi)

# print(math.sqrt(64))

# print(math.factorial(20)) # 5! -- 5 * 3 * 2 * 1

# print(10//3)
# print(math.ceil(11/3))

# Input and Output Statements

# v1 = int(input("Enter first number:- "))
# v2 = int(input("Enter second number:- "))
 
# print(v1 + v2)

# val = eval(input("Enter a value:- ")) # str
# print(val, type(val))

# command line arguments --

# from sys import argv

# print(argv-1) # ["filepath",] #  django --

# for loop()

# print(10, 20, "30 40") # min 0 max n of value *values

# print("a", "b", "c", "d", "e",sep=" ")

# print(10, end="-")  # 10-20,30
# print(20 ,end=",")
# print(30)

# s = "vfgff dugdgt \nruutshkgetiktwu \nwroiiv asd"
# print(s)

# ctrl +g -- to jump on specified line

# format

# "Mai nikla__leke" -- Gadi

# val1 = 10
# val2 = 40

# print("summation of {} and {} is {}".format (val1, val2, val1+val2))

# print(f"summation of {val1} and {val2} is {val1+val2}")

# %i == int
# %d == int
# %s == string
# %f == float

# x, y, z = 10, 20.5, "abcd"
# print("value of x is %i" %x)
# print("value of y is %f" %y)
# print("value of z is %s" %z)





# >>> a = 10
# >>> b = 20
# >>> if a == b:
# ...     print("valid")
# ...
# >>> 10 and 20 and 30 and 40
# 40
# >>> 10 and 0 and 30 and 40 and 50
# 0
# >>> 10 and 0 and 30 and 40 and 50 and False
# 0
# >>> bool(10)
# True
# >>> bool (0)
# False
# >>> 0 and 1 and 0 and 0 and 0
# 0
# >>> False or True
# True
# >>> False or True or False or False
# True
# >>> False or "" or False or False
# False
# >>> bool("")
# False
# >>> False or " " or False or False
# ' '
# >>> bool("False")
# True
# >>> bool(False)
# False
# >>> bool(0)
# False
# >>>
# >>> bool(False)
# False
# >>> bool(True)
# True
# >>>
# >>>
# >>> not 0
# True
# >>> not " "
# False
# >>> not ""
# True
# >>> not " "
# False
# >>> not {}
# True
# >>> a = 2
# >>> a = a + 2
# >>> a
# 4
# >>> a += 2
# >>> a
# 6
# >>> a -= 2
# >>> a
# 4
# >>> a *= 2
# >>> a
# 8
# >>> a **= 2
# >>> a
# 64
# >>> (10+2) * 2
# 24
# >>> 10+2 *2
# 14
# >>> "10" + "20"
# '1020'
# >>> int("abc")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: invalid literal for int() with base 10: 'abc'
# >>> int("10")
# 10
# >>> int("10.5")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: invalid literal for int() with base 10: '10.5'
# >>> float("10.5")
# 10.5
# >>> list("abcd")
# ['a', 'b', 'c', 'd']
# >>> list("[1,2,3]")
# ['[', '1', ',', '2', ',', '3', ']']
# >>> eval("10+20*50//8**2")
# 25
# >>> a = eval("10")
# >>> type(a)
# <class 'int'>
# >>> a = eval("115.5")
# >>> type(a)
# <class 'float'>
# >>> a
# 115.5
# >> a = eval("[10,20,30,40]")
# >>> a
# [10, 20, 30, 40]
# >>> type(a)
# <class 'list'>
# >>> type("10")
# <class 'str'>
# >>> type("10", "20")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: type() takes 1 or 3 arguments
# >>>