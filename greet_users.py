def greet_users(users):
    #for user in users:
    msg = "Hello, " + users.title() + "!"
    print(msg)
usernames = 'Test'
greet_users(usernames)   
def build_profile(**kwargs):
    profile = {}
    for key, value in kwargs.items():
        profile[key] = value
    return profile
user_profile = build_profile(first='Test', last='Test', age=25)
user_profile = build_profile(first='Test', last='Test', age=25,location = 'USA', type = 'Farmer')
print(user_profile)
