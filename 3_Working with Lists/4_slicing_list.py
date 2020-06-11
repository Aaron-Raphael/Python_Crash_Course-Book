blinders = ['arthur' , 'john' , 'tommy' , 'finn' , 'ada' , 'polly' , 'michael' , 'lizzie']

# slicing al list by indexing
shelby = blinders[:5]
print(shelby)

non_shelby = blinders[5:]
print(non_shelby)

grey = blinders[-3:-1]
print(grey)

# looping by slicing

for name in blinders[:5]:
    print(name.title(), "is a Shelby")

# copying by slicing 
# modifing sliced list does not affect original
main_roles = blinders[:]
print(main_roles)