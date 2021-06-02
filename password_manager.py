from menu import menu, create, find_app

choice = menu()

while choice != 'Q':
    if choice == '1':
        create()
    if choice == '3':
        find_app()
    else:
        choice = menu()
exit()
