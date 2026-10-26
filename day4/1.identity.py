# Identity operator: check if the variable and the memory location of the variable are same
# value same = location same

a = 10
b = 10
c = 5

# 1.is : if memory location is same then return true else false
print(a is b)  # checks memory lcoation as well other same as ==
print(a is c)

print(id(a))
print(id(b))
print(id(c))

# 2.is not : if memory location is not same then return true else false
print(a is not b)
print(a is not c)
