# classes can be inmported as a sinngle module or multiple module
from car_all import Car,ElectricCar

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()


# importing entire module
import car_all

my_beetle = car_all.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = car_all.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())


# importing entire class
from car_all import *

my_beetle = car_all.Car('volkswagen', 'polo', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = car_all.ElectricCar('tesla', 'cyber truck', 2019)
print(my_tesla.get_descriptive_name())