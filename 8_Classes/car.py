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
