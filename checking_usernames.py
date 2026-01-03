current_users = ['angrybalint', 'tanqr', 'badpig', 'marky', 'spring']

new_users = ['angrybalint', 'kismalac', 'badpig', 'chipy', 'hamburger']

for new_user in new_users:
    if new_user in current_users:
        print (f"This username is taken, please enter a new one.")
    else:
        print (f"This username is available. Enjoy your username!")