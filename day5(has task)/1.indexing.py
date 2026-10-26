# Indexing : access a single data or character from sequence
# list and tuple are ordered data so indexing can be used
# sets and disctionary cannot be used

a = "Python"
# index/position
# P = 0
# y = 1
# t = 2
# h = 3
# o = 4
# n = 5

# print out t
# print(a[2]) prints t
# print(a[4]) prints o

# for list
#b = ['access', 'single', 'data', 'character', 'from', 'sequence', 'print']
# prints data
#print(b[2])

#print(b[-1])  # prints out last data which is print

#c = "I am learning ( python"  # space is also index
# print out (
#print(c[14])

# define a tuple and print some data from it
#tuple = ('hello', 'mrbeast')
#print(tuple[1]) prints mrbeast

# in dictionary keys are used to access the values
my_dict = {"name": "ram", "age": 30, 5: "hello", "users": {
    "name": "sita", "age": 50, "address": "bkt"}}
print(my_dict["age"])
print(my_dict[5])
print(my_dict["users"])
print(my_dict["users"]["name"])
print(my_dict["users"]["address"])
