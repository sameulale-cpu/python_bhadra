# get user ko age
# if age is less than 18 print out "not Eligible for license"
#     ask if they want to get license or not(y/n):
#          if yes: print a statement
#          if no: print a statement
# if age is greater than or equal to 18 print out "Eligible for license"
#     ask if they have license(y/n):
#        if yes: print a statement
#        if no: ask if they want to get a license(y/n)
#              if y: print a statement
#              if n: print a statement

Age = int(input("Enter your age:"))

if Age < 18:  # Parent Block
    print("Not Eligible for license")
    user_response = input("do u want to get license(yes/no):")
    if user_response == "yes":
        print("Not Eligible right now")
    elif user_response == "no":
        print("Sad")
    else:
        print("Invalid")
elif Age >= 18:
    print("Eligible for license")
    user_response1 = input("do u want to get license(yes/no):")
    if user_response1 == "yes":
        print("Eligible right now")
    elif user_response1 == "no":
        print("Okay")
    else:
        print("Invalid")
