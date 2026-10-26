# Mark Evaluatore
# get mark from user
# if the entered marks is greater than 90 and less than 100, print a statement ("Excelent")
# if the entered marks is greater than 80 and less than 90, print a statement
# if the entered marks is greater than 70 and less than 80, print a statement
# if the entered marks is greater than 60 and less than 70, print a statement
# if the entered marks is greater than 50 and less than 60, print a statement
# if the entered marks is greater than 40 and less than 50, print a statement
# if the entered marks less than 40, print a statement
# if the mark is greater than 100 or less than 0 then print out a statement("invalid data")
# ask to rerun the Mark Evaluator, if yes rerun the Mark Evaluator, if no end the loop

rerun = "yes"

while rerun == "yes":
    try:
        Marks = int(input("Enter marks:"))

        if Marks >= 90 and Marks <= 100:
            print("Excellent A+")
        elif Marks >= 80 and Marks <= 90:
            print("A")
        elif Marks >= 70 and Marks <= 80:
            print("B+")
        elif Marks >= 60 and Marks <= 70:
            print("B")
        elif Marks >= 50 and Marks <= 60:
            print("C+")
        elif Marks >= 40 and Marks <= 50:
            print("C")
        elif Marks <= 40 and Marks >= 0:
            print("Fail")
        elif Marks > 100 or Marks < 0:
            print("Enter marks between 0 and 100")
    except:
        print("Invalid Data, try again")

    rerun = input("Do you want to rerun the loop(yes/no):")

    if rerun == "no":
        print("Loop ended")
        break
