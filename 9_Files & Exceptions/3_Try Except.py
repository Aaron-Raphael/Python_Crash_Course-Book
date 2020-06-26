print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    
    try:    # if no error continues and returns ansuer
        answer = int(first_number) / int(second_number)
        
    except ZeroDivisionError:   # if mentioned error occurs prinrs the statement
        print("You can't divide by 0!")
    
    else:   # if the except block is false else block is executed
        print(answer)
