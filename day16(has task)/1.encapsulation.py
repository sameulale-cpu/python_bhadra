# Encapsulation: binds the properties into a single unit, data hiding/attribute and methods private,
# "__" is followed by attributes or methods name to make them private
# to access private properties , a public methods should be used

class login:
    def get_info(self, username, password):
        self.__username = username
        self.__password = password

    def __detail(self):  # public method
        print(f"Username: {self.__username}, Password: {self.__password}")

    def show(self):
        return self.__detail()


p1 = login()  # cant be accessed through object
p1.get_info("ram", "ram123")
p1.show()
# p1.__detail()
# print(p1.__username)
# print(p1.__password)
