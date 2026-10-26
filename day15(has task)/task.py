# todo:
# create a class animal with attributes: eye, ear, legs, .....
# methods: sound, movement, ..., ...

# create a class dog that extends/inherits animal class with attribute name, ...
# methods: get name/details, sound, movement

# create a class bird that inherits animal class with name attribute,... methods: get name/details, sound, movement, ....

class Animal:
    eyes = None
    ears = None
    hands = None
    legs = None

    def get_details(self, eyes, ears, hands, legs):
        self.eyes = eyes
        self.ears = ears
        self.hands = hands
        self.legs = legs

    def sound(self):
        print("Animal makes a sound")

    def movement(self):
        print("Animal moves")


class dog(Animal):
    name = None

    def name(self, name):
        self.name = name

    def details(self):
        print(f"""Name: {self.name}
Eyes: {self.eyes}
Ears: {self.ears}
Hands: {self.hands}
legs: {self.legs} """)

    def sound(self):
        print("Barks.")

    def movement(self):
        print("Dog walks in 4 legs.")


class Bird(Animal):
    name = None

    def name(self, name):
        self.name = name

    def details(self):
        print(f"""Name: {self.name}
Eyes: {self.eyes}
Ears: {self.ears}
Hands: {self.hands}
legs: {self.legs} """)

    def sound(self):
        print("Bird chirp.")

    def movement(self):
        print("Bird flies using its wings.")


d1 = dog()
d1.get_details(2, 2, 0, 4)
d1.name("Tom")
d1.details()
d1.sound()
d1.movement()

b1 = Bird()
b1.get_details(2, 2, 0, 2)
b1.name("Tweet")
b1.details()
b1.sound()
b1.movement()