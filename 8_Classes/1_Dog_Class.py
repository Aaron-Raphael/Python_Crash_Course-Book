# class is a set of instruction for how to make an instance
# classes are declared in title case

class Dog():
    """ a atempt to create a dog """

    """  The __init__() method  is a special method
    Python runs automatically whenever we 
    create a new instance based on the Dog class. """
    
    def __init__(self , name , age):
        """ initialise name and age argument """
        self.name = name
        self.age = age

    def sit(self):
        """ simulate dog sitting to command """
        print(self.name.title() + ' is sitting now')

    def roll_over(self):
        """ simulate dog rolling over to command """
        print(self.name.title() + ' rolled over')

my_dog = Dog('tiny' , 4)

# the vaiables in the class are accessed by " self.name "
print("My dog's name is " + my_dog.name.title())
print("My dog is " + str(my_dog.age) + " years old")

# the methods in the class can also be accessed by dot operator " self.method() "
my_dog.sit()    # self.method()
my_dog.roll_over()

# multiple instances can be called
my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

print('\n')
print("My dog's name is " + my_dog.name.title())
print("My dog is " + str(my_dog.age) + " years old")
my_dog.sit()

print('\n')
print("Your dog's name is " + your_dog.name.title())
print("Your dog is " + str(your_dog.age) + " years old")
your_dog.sit()