# todo:
# create a class Account
# with attribute acc_number, balance, user name, address, contact,... attributes
# and get details/ constructor, add amount: get amt from user add it to balance, show detail: display acc_number, balance, username, add, contact,... methods
# create 3 objects

class Account():
    accnumber = None
    balance = None
    username = None
    address = None
    contact = None

    def getdetails(self, Acc_number, Balance, Username, Address, Contact):
        self.accnumber = Acc_number
        self.balance = Balance
        self.username = Username
        self.address = Address
        self.contact = Contact

    def addamount(self, amount):
        self.balance = self.balance + amount

    def show_detail(self):
        print(f"""Account number: {self.accnumber}
Balance: {self.balance}
Username: {self.username}
Address: {self.address}
Contact: {self.contact} """)


User1 = Account()
User1.getdetails(1, 100, "Ram", "Kathmandu", "9800000000")
User1.addamount(500)
User1.show_detail()

User2 = Account()
User2.getdetails(2, 200, "Sam", "Kathmandu", "9700000000")
User1.addamount(400)
User1.show_detail()

User3 = Account()
User3.getdetails(3, 300, "Hari", "Kathmandu", "9600000000")
User1.addamount(500)
User1.show_detail()