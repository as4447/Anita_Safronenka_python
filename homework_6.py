
class AddressBook:
    def __init__(self, name, age, height, weight, sex):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.sex = sex

#    def calc_bmi(self, weight, height):
#        bmi = round((self.weight / self.height ** 2), 2)        

    def __str__(self):
        return ", ".join([self.name, self.age, self.height, self.weight, self.sex])
        

address_book = []
print ("""Select operation: \n ------------------- \n [C] Add new user \n [R] Show user information \n [U] Update user information\n [D] Delete user \n ------------------- \n [L] Show all users \n [Q] Quit \n ------------------- \n Please enter your choice: \n """)
while True:
    choice = input("Choice: ")
    if choice == str("C"):
        address_book.append(AddressBook(input("Input name: "), input("Input age: "), input("Input height: "), input("Input weight: "), input("Input sex: ")))
    elif choice == str("R"):
        input("enter contact name: ")
        pass
    elif choice == str("U"):
        pass
    elif choice == str("D"):
        pass
    elif choice == str("L"):
        print(*[contact for contact in address_book], sep="\n")
    elif choice == str("Q"):
        exit()