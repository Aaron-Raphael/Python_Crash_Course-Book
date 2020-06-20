def name_swap(n_list):
    n_list[0],n_list[-1] = n_list[-1],n_list[0]
    return n_list

name = ['aaron' , 'raphaeel']

print(name_swap(name[:]))   # slice to carry function without altering list 
print(name)

print('\n')

print(name_swap(name))# alters list
print(name)