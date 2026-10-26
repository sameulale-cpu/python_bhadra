# Ecom
# define a list of dictionary of userdetail with username, password, usertype(buyer/seller) or store it in a file
#  {"ram":{'password':"1234", 'usertype':"buyer"}} or {'username':'ram','password':'1234','usertype':'buyer'}
# define a list of dictionary of product with name, price, seller_name or store it in a file


# get userdetail username, password from user
# check if the entered detail is  correct,
# if no: preint a statement
# if yes: login success, get usertype from the dictionary
#       if the usertype is buyer:
#           show 1. view all product, 2. Buy product, ask the product they want to buy,get the product from dictionary and access the price,get quantity from user then print the total
#       if usertype is seller:
#           show 1: view my product, 2. add product(name, price, seller_name(logined_user_name)), add it to the dictionary

userdetail = {"ram": {'password': '1234', 'usertype': "buyer"},
              "james": {'password': '1234', "usertype": 'seller'}}

product = {"headphones": {'price': '3000', "seller_name": "Adam"},
           "mouse": {"price": "2000", "seller_name": "Adam"}}

username = input("Enter username:")

if username not in userdetail:
    print("Username doesn't exist")
else:
    password = input("Enter password:")

    if password != userdetail[username[password]]:
        print("Invalid password:")
    else:
        print("Login success")

if userdetail[username['usertype']] == "buyer":
    print("1.View all products")
    print("2. Buy products")

    choice = int(input("Enter choice 1 or 2:"))

    if choice == 1:
        product
        


if userdetail[username['usertype']] == "seller":
    print("1.View my product")
    print("2.Add products")