# a = "Hello"
# print(a.lower())
# print(a.capitalize())
# print(type(a)) # class str: is already defined

# Structure
# class str:
#     def lower():
#         print("this is a function inside a class")

#     def capitalize(self):
#         print("This Is Capitalize")

# constructor : method that is automatically executed during object creation

# Using method:
# class House:
#     # floor = 2 # attributes:floor, rooms, windows, door, stairs
#     rooms = None
#     windows = None
#     doors = None

#     def details(self, room, window, door):  # functions defined insdie class are methods
#         print("This is a function inside a House class")
#         self.rooms = room  # h1.rooms
#         self.windows = window
#         self.doors = door

#     def show(self):
#         self.details()
#         print(f"""Rooms: {self.rooms}
# Windows: {self.windows}
# Doors: {self.doors} """)

# Using constructor:
class House:
    def __init__(self ,room, window, door):
        self.rooms = room  
        self.windows = window
        self.doors = door

    def show(self):
        self.__init__()
        print(f"""Rooms: {self.rooms}
Windows: {self.windows}
Doors: {self.doors} """)

h1 = House(2, 4, 6)  # in self parameter h1 goes as value
# h1.details(2, 4, 6)
# h1.__init__(1, 2, 3)
print(h1.rooms)
print(h1.windows)
print(h1.show())


# h2 = House()
# h2.floor = 4
# print(h2.floor)


