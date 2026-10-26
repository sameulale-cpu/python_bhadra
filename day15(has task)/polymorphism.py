# Polymorphism: poly : multiple, morph : form
# different class with same method name
# functionality of the method depends on the object

a = 10
b = 5

x = "a"
y = "ball"

print(a + b)
print(a.__add__(b))
print(x + y)
print(x.__add__(y))

class int:
    def _add__(self):
        print("addition of integer")

class str:
    def __add__(self):
        print("concatenate string")


class Dog:
    def move(self):
        print("Dog moves using leg.")


class Bird:
    def move(self):
        print("Bird moves using wings.")


d1 = Dog()
b1 = Bird()

d1.move()
b1.move()
