# Object oriented Programming: 

# object: real world entity , data created using the class
# class: structures, blueprints

# Syntax:
# class class_name:
#     attributes : variables inside class e.g. a = 10, if inside function then their called local variable
#     methods

#a = class_name()  , a is data created using class
# class call, a is an object 

class House:
    floor = 2 # attributes:floor, rooms, windows, door, stairs
    rooms = 8
    windows = 8
    door = 9
    stairs = 2

h1 = House() # House(): House class lai call, h1 is an object/instant of house class

print(h1.floor)
h1.floor = 3
print(h1.floor)

h2 = House()
h2.floor = 4
print(h2.floor)

# create a class Car
# add attributes (....)
# create 3 objects using class

class car():
    steering_wheel = 1
    sits = 4
    wheels = 4
    glass = 6
    car_door = 4
    max_speed = 200
    power = 100
    size = 100

lambo = car()
lambo.max_speed = 400
lambo.power = 350
lambo.sits = 2
lambo.size = 165

bugatti = car()
bugatti.max_speed = 500
bugatti.power = 380
bugatti.size = 200

tesla = car()
tesla.max_speed = 250
tesla.size = 150
tesla.power = 120