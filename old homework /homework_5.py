your_login=input("enter your login:")

def check_login(get_amount):
	def my_wrapper(your_login):
		if your_login == "Python":
			get_amount(your_login)
		else:
			print("You don't have permissions to view a account balance")
	return my_wrapper

@check_login
def get_amount (your_login):
	  print(f'{your_login} has 200$') 
	  
	
get_amount=check_login(get_amount)
get_amount(your_login)

# input
#print("Enter your login")
#login = input()

# function
#def print_balance():
    #print ("Your balance is 1$")

# decorator
#def my_decorator(print_balance):
    #def my_wrapper():
        #if login == "admin":
           # print_balance()
        #else:
            #print ("You don't have permissions to view a account balance")
    #return my_wrapper'''

# create decorator and call orig func
#print_balance = my_decorator(print_balance)
#print_balance()
