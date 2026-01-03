usernames = ['person', 'someone', 'admin', 'owner', 'me']

for username in usernames:
    if username == 'admin':
        print (f"Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in.")

if usernames == []:
   print ("We need to find some users!")