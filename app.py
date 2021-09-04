Telephone_Book = {
    '1111111111':'Amal',
    '2222222222': 'Mohammed',
    '3333333333': 'Khadijah',
    '4444444444': 'Abdullah',
    '5555555555':'Rawan',
    '6666666666':'Faisal',
    '7777777777':'Layla',
    'amal':'1111111111',
    'mohammed': '2222222222',
    'khadijah': '3333333333',
    'abdullah': '4444444444',
    'rawan':'5555555555',
    'faisal':'6666666666',
    'layla':'7777777777'
}

############
# Functions 
############

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

# Stores the user value, to run the respective operation.
command = ""

while True:
    command = input('''
> Select The Operation:
    1 - Search By Number
    2 - Search By Name
    3 - Add a Name to The Telephone Book
    4 - Print The Telephone Book
    5 - Quit The Program
> ''')
    if command == "1":
        search_by_number()
    elif command == "2":
        search_by_name()
    elif command == "3":
        add_number()
    elif command == "4":
        print(Telephone_Book)
    elif command == "5":
        print("See you soon.")
        break
    else:
        print("Invalid input")
