from data import *

# To Search By Number 
def search_by_number():
    x = input("> Enter the Number: ")
    if x.isdigit() and len(x) == 10:
        x = str(x)
        if x in Telephone_Book:
            print(Telephone_Book[x])
        else:
            print("Sorry, the number is not found.")
    else:
        print("This is invalid number.")

# To Search By Name
def search_by_name():
    x = input("> Enter the name: ").lower()
    if x in Telephone_Book:
        print(Telephone_Book[x])
    else:
        print("Name not found.")

# To Add a name to the telephone book
def add_number():
    x = str(input("> Enter The Name: ")).lower()
    if x in Telephone_Book:
        print("The Name already registered.")
    else:
        y = input("> Enter The Number: ")
        if y.isdigit() and len(y) == 10:
            Telephone_Book[x] = y
            Telephone_Book[y] = x
        else:
            print("Invalid Number")
