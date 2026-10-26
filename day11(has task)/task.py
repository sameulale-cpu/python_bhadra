# Accounting
# create a dictionary with user detail(username, password) username key, password value
# create a dictionary with user balance(username, balance) username key, balance value
# user_detail = {"Sam": "Sam12345", "Hari": "Hari12345"}
# user_balance = {"Sam": 1000, "Hari": 2000}

# register/Login
# if choice register
# get username and password from user and store the data in a file
# if choice is login
# get username and password from user

# check if the username exist in the file (y/n):
#  if no print a statement("User does not exist")
#     if yes, check if the entered password is equal to the password in the dictionary(y/n)
#        if no, print a statement("Invalid credential")
#        if yes, show 2 choice. 1. Show detail, 2. Add balance, 3. Withdraw
#              if user choice 1: show the user balance from the file
#              if user choice 2: get amount to add from user, get balance from the file and add the amount with the balance, print the total balance
#              if user choice 3: get amount to withdraw,  get balance from the file, check if the amount is less than balance(y/n), if yes subtract amount from balancew, if no print out insufficient balance

user_input = input("Do you want to Register or Login:")

user_infile = False
right_password = False


def check_username_exists():
    global user_infile, right_password
    file = open("day11(has task)/user.txt", "r")
    readlines = file.readlines()

    for i in readlines:
        data = i.strip().split(",")
        registered_username = data[0]
        registered_password = data[1]
        if username == registered_username:
            user_infile = True

            if password == registered_password:
                right_password = True
            else:
                print("Wrong password")
            break

        file.close()

    if not user_infile:
        print("Username doesn't exist")
    return user_infile, right_password


def details():
    file = open("day11(has task)/balance.txt", "r")
    for i in file:
        data = i.strip().split(",")

        user = data[0]
        balance = float(data[1])

        if username == user:
            print("Username:", username)
            print("Balance:", balance)
            break
    file.close()


def add():
    file = open("day11(has task)/balance.txt", "r")
    lines = file.readlines()
    file.close()

    file = open("day11(has task)/balance.txt", "a")
    for i in lines:
        data = i.strip().split(",")

        user = data[0]
        balance = float(data[1])

        if username == user:
            print(f"Your current balance is: {balance}$")
            amount = float(input("Enter the value to add in your account:"))
            balance = balance + amount
            print(f"Your total balance now is: {balance}$")

    file.close()


def withdraw():
    amount = float(input("Enter amount to withdraw:"))

    file = open("day11(has task)/balance.txt", "r")
    lines = file.readlines()

    file = open("day11(has task)/balance.txt", "a")
    for i in lines:
        data = i.strip().split(",")
        user = data[0]
        balance = float(data[1])

        if user == username:
            if amount <= balance:
                balance = balance - amount
                print("Successfully withdrawn ")
                print(f"Your Current balance is: ${balance}")
            else:
                print("Insufficient balance")
    file.close()


while user_input.lower() == "register":
    username = input("Enter your username:")
    password = input("Enter password:")

    file = open("day11(has task)/user.txt", "a")
    a = file.write("\n" + username + "," + password)
    file.close()

    g = open("day11(has task)/balance.txt", "a")
    b = g.write("\n" + username + "," + "0")
    g.close()

    print("Registration successful!")

    user_input = input("Do you want to Register or Login:")

if user_input.lower() == "login":
    username = input("Enter your username:")
    password = input("Enter password:")

    check_username_exists()
    # print("hello")

    if (user_infile == True) and (right_password == True):
        print("Login successfull")
        rerun = "yes"

        while rerun == "yes":
            print("1.Show details")
            print("2.Add balance")
            print("3.Withdraw")

            choice = input("Enter choice between 1,2 and 3:")

            if choice == "1":
                details()
            elif choice == "2":
                add()
            elif choice == "3":
                withdraw()
            else:
                print("Invalid choice.")

            rerun = input("Do you want to choose again:(yes/no):").lower()

            if rerun == "no".lower():
                print("End")
                break


# if username not in user_detail:
#     print("User doesnt exist")
# else:
#     password = input("Enter password:")
#     if password != user_detail[username]:
#         print("Invalid credential")
#     else:
#         print("Login successfully")

#         print("1.Show details")
#         print("2.Add balance")
#         print("3.Withdraw")

#         choice = int(input("Enter choice between 1,2 and 3:"))

#         if choice == 1:
#             details()
#         elif choice == 2:
#             add()
#         elif choice == 3:
#             withdraw()
#         else:
#             print("Enter valid choice:")


# for i,j in user_detail.items():
#     if i == username and j == password:
#         login = True

#     if login:
#         print("Enter choices 1,2,3:")
#     else:
#         print("Invalid credentials")
