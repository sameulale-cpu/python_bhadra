# get a greeting from user
# get the number of time they want to print greeting from user
# using while loop, print out the greeting according to the entered number

Greeting = input("Enter greeting:")
many = int(input("How many times do u want to print greeting:"))
count = 0

while count < many:
    print(Greeting)
    count += 1
