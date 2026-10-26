# Slicing : get a subset of data from the given sequence
# start index: inclusive: data is included
# end index: exclusive: data is not included

# a[start_index : end_index + 1: step]

# print mind
a = "mindrisers"
print(a[0: 4])  # prints mind
print(a[0:])  # gives full print
print(a[:])  # gives full
print(a[0: 10: 1])  # same
# m = first index = first data (takes every second item), prints mnrsr
print(a[0: 10: 2])
print(a[0: 10: 3])  # prints mdss

# print out rise
print(a[4: 8])

# print out risers
print(a[4: 10])

# print out mindrise
print(a[0: 8])

b = ['access', 'single', 'data', 'character', 'from', 'sequence', 'print']

# print data from index 1 to 4
print(b[1: 5])

# print from 0 to 3
# print(b[0:4])

# print from index 2 to 5
# print(b[2: 6])

# print out data in odd index
# print(b[1: 7: 2]) #prints ['single', 'character', 'sequence']

# print out the data in even index
# print(b[0: 7: 2]) #prints ['access', 'data', 'from', 'print']

# print out the data in every 3 step
print(b[0: 7: 3])

# print reverse of the list
print(b[ : : -1])