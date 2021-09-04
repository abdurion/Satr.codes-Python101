from data import *

# To Search By Number 
def search_by_number():
    x = input("> Enter the Number: ")
    if x.isdigit() and len(x) == 10:
        x = int(x)
        if x in Telephone_Book:
            print(Telephone_Book[x])
        else:
            print("Sorry, the number is not found.")
    else:
        print("This is invalid number.")

# To Search By Name
def search_by_name():
    x = input("> Enter the name: ").capitalize()
    for key, value in Telephone_Book.items():
        if x == value:
            return print(key)
    print("Name not found.")

# To Add a name to the telephone book
def add_number():
    x = input("> Enter The Name: ").capitalize()
    if x in Telephone_Book:
        print("The Name already registered.")
    else:
        y = input("> Enter The Number: ")
        if y.isdigit() and len(y) == 10:
            y = int(y)
            Telephone_Book[y] = x
        else:
            print("Invalid Number")
