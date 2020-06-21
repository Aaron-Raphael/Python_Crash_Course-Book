# ** is ured to create a dictionary and story arbitary numbber of keywork arguments

def build_profile(first,last,**user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,val in user_info.items():
        profile[key] = val
    return profile

user_profile = build_profile('aaron' , 'raphael' , 
                            location = 'cbe' ,
                            field = 'mechanical')
print(user_profile)