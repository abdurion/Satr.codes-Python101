from helpers import *

# Stores the user value, to run the respective operation.
command = ""
while True:
    command = input('''
> Select The Operation:
    1 - Search By Number
    2 - Search By Name
    3 - Add a contact to The Telephone Book
    4 - Print The Telephone Book
    5 - Quit The Program
> ''')
    if command == "1":
        search_by_number()
    elif command == "2":
        search_by_name()
    elif command == "3":
        add_contact()
    elif command == "4":
        print(Telephone_Book)
    elif command == "5":
        print("See you soon.")
        break
    else:
        print("Invalid input")
