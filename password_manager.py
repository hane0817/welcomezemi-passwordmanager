from menu import menu, create

choice = menu()

while choice != 'Q':
    if choice == '1':
        create()
    else:
        choice = menu()
exit()
