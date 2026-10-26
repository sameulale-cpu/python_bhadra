# Args:tuple of positional arguments , used when not fixed arguments
# multiple positional arguments are accepted by a parameter
# an args is defined by "*"

# def user(name, *args): # name is guranteed name = "Ram" here
#     print(args)
#     for i in args:
#         print(i)

# n = "Ram"
# c = "9+8998"
# a = "Address"
# user(n,c,a)

# user(name = n, contact = c, add = a)
# user(contact = c, name = n, add = a, age = 15)
# user(n,c,a,15)
# user(n,c,a,15,"ram@gmail.com")

# Kwargs: dictionary of keyword arguments
# a kwargs is defined by "**"

# def user(**kwargs):
#     print(kwargs)
#     print(kwargs.items())  # items methods and others too , list of tuples
#     print(kwargs.values)
#     print(kwargs.keys())
#     for i, j in kwargs.items():   # i = key , j = values 
#         print(f"{i}:{j}")


# n = "Ram"
# c = "9+8998"
# a = "Address"
# user(name=n, contact=c, address=a)
# user(name=n, contact=c, address=a, age=15)
# user(name=n, contact=c, address=a, age=15, email="ram@gmail.com")

# requirement: add 2 numbers using sum function then multiply it by 3
# return: A data is returned to the line of function call, also ends the function

# def multiply(d):  # d= 15
#     e = d * 3
#     return e


# def sum(a, b):  # function define
#     c = a + b  # 10 + 5 = 15
#     f = multiply(c)
#     return f
#     print(c * 3)  # doesnt work under return


# sum(10, 5)

# a = "hello" whenver a data is returned from a function or method store it in a variable for later purpose
# b = a.capitalize()
