file_name = 'programming.txt'
# 'w'-write mode 'r'-read mode 'a'-append mode
with open(file_name , 'w') as file_object:
    file_object.write('I love programing\n')

with open(file_name , 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")