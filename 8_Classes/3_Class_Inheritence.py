# inheritance
# if the new class is annothet form off another class then use inheritence

class Car():
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading =0    # default values can set to an attribute
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
        
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage): # defining method to update value
        """Set the odometer reading to the given value."""
        if mileage>= self.odometer_reading:
            self.odometer_reading = mileage

    def increment_odometer(self, miles): # method to increment odometer  reading
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles 

    def fill_gas_tank(self):
        print("you have enough gas for today")


# creating inherited class

# instance as classes
# you  can break the code and define in seperate class and include in code
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



my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.assistant.describe_assistant()