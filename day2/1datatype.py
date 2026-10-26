# Datatype

# 1. string: alphabets , numbers , special characters
# define using ['...',"...",'''...''',""""...""""]
a = 'this is a line\' s 123 #$'
b = "this is a  'line"
c = ''' 
this is
test
'''
# print(a)
# print(type(a))
# print(c)

# 2. integer: whole number
a = 10  # overwrite: a variable has both string and integer assigned to it , calls the closest variable
#print(type(a))

# 3. float : decimal number
a = 10.5
#print(type(a))

# 4. boolean data
a = True
b = False

# None type
a = None  # for later adding values

# 5. Group datatype
# a. List: [] is used to define list ,can contain multiple data of multiple types , mutable(changeable), ordered
my_list = [1, 2, 3, 4, "hi", "hello", 15.55, 20.5]
print(my_list)
print(type(my_list))

# b. Tuple: () used to define tuple ,can contain multiple data of multiple datatype, ordered,
# immutable(unchangeable) for holding constant data
my_tuple = (1, 2, 3, 4, "hi", 15.55)
print(my_tuple)
print(type(my_tuple))

# c.Set: {} used to define set, can contain multiple datatype, unordered, not contain duplicate data
my_set = {1, 2, 3, 4, "hi", 15.55, "hi", 2}
print(my_set)
print(type(my_set))

# d. Distionary: {} used to define disctionary, key:value pair -> a data
my_dict = {"key": "value", 1: 10, "name": "ram", "age": 35}
print(my_dict)
print(type(my_dict))
