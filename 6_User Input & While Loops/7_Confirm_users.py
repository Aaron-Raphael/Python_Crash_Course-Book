unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop() # pop removes the last item from list

    print('verifying user :',current_user)
    confirmed_users.append(current_user)

print('followinng are confirmed :')
for user in confirmed_users:
    print('\t',user)