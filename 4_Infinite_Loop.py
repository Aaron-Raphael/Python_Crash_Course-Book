#you cann use += to add strings to strings too
prompt = '\n tell something and i will tell it back :'
prompt += '\n enter " quit " to quit :'

# infinite while loop with exit command
# a flag is used to check multiple conditions
# here flag is active

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print('\t' + message)