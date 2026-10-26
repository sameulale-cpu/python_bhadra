# Pillars of OOP
# Inheritance: super - sub class, parent-child class , base-derived class
# a properties of a class is inherited by another class
# child class can use the attributes and methods of parent class
# child class can have unique attributes and methods 
# parent class and child class can have method with same name 

class Car:
    model = None
    brand = None
    color = None
    speed = 150

    def get_details(self, model, brand, color):
        self.model = model
        self.brand = brand
        self.color = color

    def show_details(self):
        print(f"""Model: {self.model}
Brand: {self.brand}
Color: {self.color} """)

# Below Car is super/parent class. Ev class le Car class ko property inherit gareko

class EV(Car):
    pass
    speed = None

    def get_speed(self, speed):
        self.speed = speed


ev1 = EV()
print(ev1.brand)
ev1.get_speed(250)


# Polymorphism
# Encapsulation
# Abstraction
