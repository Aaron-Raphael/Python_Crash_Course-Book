# importing module inside a module
from car import Car

class Assistant():
    """attempt to model a assistant"""
    def __init__(self , assistant_version = 2.0):
        """initialise assistant attribute"""
        self.assistant_version = assistant_version

    def describe_assistant(self):
        print('the A.I assistant is version', self.assistant_version)


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year) # super function makes connection between child and parent class

        self.battery_size = 70 # defining attribute for child class

        self.assistant = Assistant() # defining external class as attribute

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def fill_gas_tank(self):   #   overriding methods from the parent class 
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")
