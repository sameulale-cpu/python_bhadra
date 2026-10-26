# create a list of username
# get the username from user
# if the username exist print a statment
# if user doesnot exist print a statement
# ask to rerun the calculator, if yes rerun the calculator, if no end the loop

rerun = "yes"

while rerun == "yes":
    List = ["Hari", "Sam", "Adam"]
    User = input("Enter your username:")
    if User in List:
        print("Username exist")
    else:
        print("Done")
    rerun = input("Do you want to rerun(yes/no):")

    if rerun == "no":
        print("Loop ended")
        break