# print("hello")

# This is a comment

''' 
This is a 
multiline comment
'''

"""
This is a 
multiline comment
"""
first_name =  "Manas"

# Data Types
age = 40

#int
a = 10
b = -20
# print(a)
# print(b)
# print(type(a))
# print(type(b))

# float
c = 1.2
d = -100.0
# print(type(c))
# print(type(d))

# complex
# e = a+bj
# print(type(e))

# boolean
e = True
f = False
# print(type(e))
# print(type(f))

# Sequence Types
string = "Hello WorldWorldWorldWorldWorld"
string2 = "It's afternoon now"
string3 = 'Hello "world"'
string4 = '''Kalathia, Khandagiri," 
"Bhubaneswar, Odisha" 
"751030'''
# print(string)
# print(string[4]) 
# print(string[0:4]) 
# print(string[6:]) 
# print(string[:20]) 
# string[0] = "M" # TypeError: 'str' object does not support item assignment

# Lists
list1 = ["apple", "banana", "cherry"]
# print(list1)
# print(list1[1])
# print(list1[1:3])
# print(list1[2:])
# print(list1[:2])
# list1[1] = "blackcurrant"
# print(list1)

#Tupples
tuple1 = ("apple", "banana", "cherry")
# print(tuple1)
# print(tuple1[1])
# print(tuple1[1:3])
# print(tuple1[2:])
# print(tuple1[:2])
# tuple1[1] = "blackcurrant" # TypeError: 'tuple' object does not support item assignment

# Set Types
set1 = {"apple", "banana", "banana", "banana", "cherry"}
# print(set1)
# set1[1] = "blackcurrant" # TypeError: 'set' object does not support item assignment

#frozenset
frozenset1 = frozenset({"apple", "banana", "cherry"})
# print(frozenset1)
# frozenset1[1] = "blackcurrant" # TypeError: 'frozenset' object does not support item assignment

# Dictionary Types
dict1 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
# print(dict1)
# print(dict1["model"])
dict1["year"] = 2020
# print(dict1)

#None
var1 = None
print(var1)
print(type(var1))


result = 10.5
result  += 10
print(result)