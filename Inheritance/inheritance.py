# Parent class
class Vehicle:
    def info(self):
        print("This is a vehicle.")

# Child class inheriting from Vehicle
class Car(Vehicle):
    def car_info(self):
        print("This is a car.")

# Create an object of Car
c = Car()
c.info()       # Access parent class method
c.car_info()   # Access child class method
