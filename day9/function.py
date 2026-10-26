# Function: task sepcific, reusable

# Syntax
# def function_name():      , fxn call
#    statements

# function_name()  fxn call
#a = 10 # Global variable: can be call and used anywhere in the program

#def sum():  # defining function
#    a = 15  # local variable: can only be called and used inside this program
#    b = 5
#    print(a + b) #prints 20
#    print(a)    # prints 15

#sum() # calling function
#print(a) #prints 10

# Parameter: Variables defined inside the paranthesis in function definition
# Arguments: Variable/value inside the paranthesis in function call
# argument is passed to the parameter

#def sum(x, y, z): #x is a parameter
#    print(x + y + z)

#sum(10, 15, 20)

# types of arguments 
# 1. Positional argument: data is assigned sequential i.e. 1st para = 1st arg, 2nd para = 2nd arg, ...

# def user(name, contact, address):
#     print(f"""Name: {name}
# Contact: {contact}
# Address: {address} """)

# n = "Ram"
# c = "9+8998"
# a = "Address"
# user(n,c,a)
    
# 2. Keyword argument: direct data is assigned to parameter during function call
# def user(name, contact, address):
#     print(f"""Name: {name}
# Contact: {contact}
# Address: {address} """)

# n = "Ram"
# c = "9+8998"
# a = "Address"
# user(name = n,contact = c,address = a) # shouldnt be in order

# 3. default argument
def user(name = "Default data", contact = "Default contact", address = "Default address"):
    print(f"""Name: {name}
Contact: {contact}
Address: {address} """)

n = "Ram"
c = "9+8998"
a = "Address"
user(n, c, a) # prints Ram, ...
user() # prints default defintion(is user doesnt send any data)