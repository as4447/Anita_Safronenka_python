
login={}
def create_login(*args,**kwargs):
    global login
    while True:
        login=input("Put your login:")
        if login in login.keys():
            print("this login already exists")
        else:   
            break
        
    d1={"sex": sex, "age": age,"weight": weight, "height":height}
    height = float(input( "Your heigh:" ))/ 100
    mass = float(input("Your weight: "))
    sex = input("Your sex: ")

    Height_Squared = height * height
    BMI_Formula_Assisted = weight / Height_Squared
    BMI_Formula_Completed = BMI_Formula_Assisted * 10000
    BMI_Formula_Completed = str(BMI_Formula_Completed)
    BMI_Formula_Completed = float(BMI_Formula_Completed)
   
def show_user():
    global login 
    user=input("Put in login")
    if user in login.keys():
        for key, value in login[user].items():
            print(key + ':', value )
        else:
            print("user with this login is registered")

def change_user()
    global user
    if user in login.keys():
        while True:
            if user in login.keys():
                print("Login already exits, put the other one")
            else:
                break
        height = float(input( "Your heigh:" ))/ 100
        mass = float(input("Your weight: "))
        sex = input("Your sex: ")
        d1={"sex": sex, "age": age,"weight": weight, "height":height}
        Height_Squared = height * height
        BMI_Formula_Assisted = weight / Height_Squared
        BMI_Formula_Completed = BMI_Formula_Assisted * 10000
        BMI_Formula_Completed = str(BMI_Formula_Completed)
        BMI_Formula_Completed = float(BMI_Formula_Completed)
        
    

def add_update_user(func):
    def add_update (*args,**kwargs):
        height = float(input( "Your heigh:" ))/ 100
        mass = float(input("Your weight: "))
        sex = input("Your sex: ")
        Height_Squared = height * height
        BMI_Formula_Assisted = weight / Height_Squared
        BMI_Formula_Completed = BMI_Formula_Assisted * 10000
        BMI_Formula_Completed = str(BMI_Formula_Completed)
        BMI_Formula_Completed = float(BMI_Formula_Completed)
        return func(*args,heigh,mass, sex)
    return add_update

def delete():
    global login
    user=input("Delete user")
    if user in login.keys():
        del login(user)
        print("Login is deleted")
    else:
        print("Login does not exist")

def add_user(func):
    def update (*args,**kwargs):
        height = float(input( "Your heigh:" ))/ 100
        mass = float(input("Your weight: "))
        sex = input("Your sex: ")
        Height_Squared = height * height
        BMI_Formula_Assisted = weight / Height_Squared
        BMI_Formula_Completed = BMI_Formula_Assisted * 10000
        BMI_Formula_Completed = str(BMI_Formula_Completed)
        BMI_Formula_Completed = float(BMI_Formula_Completed)
        return func(*args,heigh,mass, sex)
    return update

def exit():
    print("Goodbye")






