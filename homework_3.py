

Weight = input("Put in your weight in KG: ")
Height = input("Put in your height in CM: ")
Weight = float(Weight)
Height = float(Height)
Height_Squared = Height * Height
BMI_Formula_Assisted = Weight / Height_Squared
BMI_Formula_Completed = BMI_Formula_Assisted * 10000
BMI_Formula_Completed = str(BMI_Formula_Completed)
print("You have a BMI score of " + BMI_Formula_Completed + ".")
BMI_Formula_Completed = float(BMI_Formula_Completed)
BMI_Formula_Completed = float(BMI_Formula_Completed)
if BMI_Formula_Completed <= 20:
	print("|20============50")
elif BMI_Formula_Completed <=23:
	print("20=|==========50")
elif BMI_Formula_Completed <=26:
	print("20==|==========50")
elif BMI_Formula_Completed <=29:
	print("20===|=========50")
elif BMI_Formula_Completed  <=30:
	print("20====|========50")
elif BMI_Formula_Completed  <=33:
	print("20=====|=======50")
elif BMI_Formula_Completed  <=36:
	print("20======|======50")
elif BMI_Formula_Completed  <=39:
	print("20=======|=====50")
elif BMI_Formula_Completed  <=40:
	print("20========|====50")
elif BMI_Formula_Completed  <=43:
	print("20=========|===50")
elif BMI_Formula_Completed <=46:
	print("20==========|==50")
elif BMI_Formula_Completed <=49:
	print("20===========|=50")
elif BMI_Formula_Completed <=50:
	print("20=============50|")
else:
	print("20=============50")


	

