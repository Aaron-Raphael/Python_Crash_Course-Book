# * represents arbitary number of arguments
# it accepts as many arguments as passed

def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)        
        
        
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# positioonal and arbiitary arguments can be passed together
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) +"-inch pizza with the following toppings:")
    
    for topping in toppings:
        print("- " + topping)
        
        
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')