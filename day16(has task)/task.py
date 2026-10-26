# todo:
# creat a class Account with attribute: username, acc_number, acc_balance, password, define private attribute
# method: login(username, password), show details(user details show), define private methods
# create 2 objects, print out all the details

class Account:
    # __username = None
    # __acc_number = None
    # __acc_balance = None
    # __password = None

    def login(self, username, password, acc_number, acc_balance):
        self.__username = username
        self.__password = password
        self.__acc_number = acc_number
        self.__acc__balance = acc_balance

    def __show_details(self):
        print(f"Username: {self.__username}, Password: {self.__password}, Account number: {self.__acc_number}, Account Balance: {self.__acc__balance}")

    def idk(self):
        return self.__show_details()


p1 = Account()
p1.login("Sam", "Sam123", 1, 1500)
p1.idk()
