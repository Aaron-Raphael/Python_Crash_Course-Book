""" modules are files containing function and saved as .py
    and can be imported and used inn other programs"""

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) +"-inch pizza with the following toppings:")    
    for topping in toppings:        
        print("- " + topping)