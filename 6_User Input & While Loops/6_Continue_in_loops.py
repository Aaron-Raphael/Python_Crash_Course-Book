# continue tells the program to continue to to next itration of loop without considering rest of the code
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)