# the middle name is made optional by  passing empty default string
def get_formatted_name(first_name, last_name, middle_name=''):    
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name

    return full_name.title()   
        

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

# passing list to fun

def name_list(n_list):
    full =''
    for name in n_list:
        full +=name.title() + ' '

    return full


name = ['aaron' , 'raphael']
print(name_list(name))