your_login=str(input("enter your login: "))


def deposit():
	  amount = float(input("Enter your amount: "))
	  your.balance+=amount
	  print("Your amount is:",amount)

def check_login(deposit):
	def my_wrapper():
		if login=="Python":
			deposit()
		else:
			print("You don't have permissions to view a account balance")
			return my_wrapper


    






