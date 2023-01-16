class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)
b = Bus('School Volvo', 180, 12)
print(b.seating_capacity())
#####################################33
class Vehicle:
    color = 'white'
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
#        self.color = 'white'
    def __str__(self):
        return 'Color: {}, Vehicle name: {}, Speed: {}, Mileage: {}'.format(self.__class__.color, self.name, self.max_speed, self.mileage)
class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass
b = Bus('SV', 180, 12)
c = Car('Audi Q5', 240, 18)
print(b)
print(c)
################
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        amt = super().fare()
        amt += amt *10 /100
        return amt

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())
#######################
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)
print(isinstance(School_bus,Vehicle))
