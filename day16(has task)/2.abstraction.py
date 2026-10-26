#Abstraction: data hiding --> hide unnecessary details/event from user

class Bike:
    key = False
    gear = False
    acc = False
    clutch = False

    def start(self):
        self.key = True
        self.gear = True
        self.acc = True
        self.clutch = True