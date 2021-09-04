from data import *

# To Search By Number 
def search_by_number():
    x = input("> Enter the Number: ")
    if x.isdigit() and len(x) == 10:
        x = int(x)
        for key, value in Telephone_Book.items():
            if x == value:
                return print(key)
        print("Sorry, the number is not found.")
    else:
        print("This is invalid number.")

# To Search By Name
def search_by_name():
    x = input("> Enter the name: ").capitalize()
    for key, value in Telephone_Book.items():
        if x == key:
            return print(value)
    print("Name not found.")

# To Add a name to the telephone book
def add_contact():
    x = input("> Enter The Name: ").capitalize()

    for key, value in Telephone_Book.items():
        if key == x:
            return print("The name is already registered.")
        else:
            y = input("> Enter the number: ")
            if len(y) == 10:
                y = int(y)
                if y == value:
                    return print("The number is already registered.")
                else:
                    break
            else:
                return print("This is invalid number")
    Telephone_Book[x] = y
    print("The contact has been added.")