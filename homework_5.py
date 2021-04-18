your_login=input("enter your login:"))

def check_login(deposit):
	def my_wrapper(*args,**kwargs):
		if args[0] == "Python":
			deposit(*args,**kwargs)
		else:
			print("You don't have permissions to view a account balance")
	return my_wrapper

def get_amount (your_login):
	  print(f'{your_login} has 200$')
	

get_amount(your_login)
