# Logical operator

a = 10
b = 1
c = 5

# and : if both conditions are true then output : true , otherwise false
# True, True = True
# True , False = False

# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)
print(a < b and a < c)

# or : if any one of the conditions true then output true, otherwise false

# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)

# not: if condition is true , output: false , vise versa (not has least priority)
# print(not True)
# print(not False)
# print(not True)
# print(not False)
print(not (a < b or a < c))
