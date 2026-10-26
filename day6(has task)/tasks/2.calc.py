# Calculator
# get 2 numbers from user
# get an operator from user(+,-,*,/)
# if operator is equal to +, then print out the sum of 2 numbers
# if operator is equal to -, then print out the subtract of 2 numbers
# if operator is *, then print out the multiplication of 2 number
# if operator is /, then print out the division of 2 number
# ask to rerun the calculator, if yes rerun the calculator , if no end the loop
# implement function

def sum():
    print("Sum is:", a + b)

def subtract():
    print("Difference is:", a - b)

def multiplication():
    print("Multiplication", a * b)

def division():
    if b ==0:
        print("Can't be divided by zero")
    else:
        print(a / b)

rerun = "yes"

while rerun == "yes":
    try:
        a = int(input("Enter first number:"))
        b = int(input("Enter second number:"))
        operator = input("Enter your operator +,-,*,/ :")
        if operator == "+":
            sum()
        elif operator == "-":
            subtract()
        elif operator == "*":
            multiplication()
        elif operator == "/":
            division()
        else:
            print("Enter valid operator")

    except:
        print("Invalid , try again")
    rerun = input("Do you want to rerun the calculator(yes/no):")

    if rerun == "no":
        print("Loop ended")
        break
