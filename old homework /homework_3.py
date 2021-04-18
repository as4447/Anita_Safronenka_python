Gender = input("Are you a male(m) or female(f): ")
Age = int(input("How old are you: "))
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

if BMI_Formula_Completed < 20 and gender == "m":
    print("Your BMI is",str(bmi)+". That means underweight")
elif BMI_Formula_Completed < 19 and gender == "f":
    print("Your BMI is",str(bmi)+". That means underweight")
elif BMI_Formula_Completed in range(20, 25) and gender == "m":
    print("Your BMI is",str(bmi)+". That means normal weight")
elif BMI_Formula_Completed in range(19, 24) and gender == "f":
    print("Your BMI is",str(bmi)+". That means normal weight")
elif BMI_Formula_Completed in range(26, 30) and gender == "m":
    print("Your BMI is",str(bmi)+". That means overweight")
elif BMI_Formula_Completed in range(25, 30) and gender == "f":
    print("Your BMI is",str(bmi)+". That means overweight")
elif BMI_Formula_Completed in range(31, 40) and gender == "m":
    print("Your BMI is",str(bmi)+". That means obesity")
elif BMI_Formula_Completed in range(31, 40) and gender == "f":
    print("Your BMI is",str(bmi)+". That means obesity")
elif BMI_Formula_Completed > 40 and gender == "m":
    print("Your BMI is",str(bmi)+". That means strong obesity")
elif BMI_Formula_Completed > 40 and gender == "f":
    print("Your BMI is",str(bmi)+". That means strong obesity")
else:
    print("Your BMI is",bmi)

 if BMI_Formula_Completed in range(19, 24) and age in range(19, 24):
    print("Your BMI is optimal for your age!")
elif BMI_Formula_Completed in range(25, 34) and age in range(20, 25):
    print("Your BMI is optimal for your age!")
elif BMI_Formula_Completed in range(35, 44) and age in range(21, 26):
    print("Your BMI is optimal for your age!")
elif BMI_Formula_Completed in range(45, 54) and age in range(22, 27):
    print("Your BMI is optimal for your age!")
elif BMI_Formula_Completed in range(55, 64) and age in range(23, 28):
    print("Your BMI is optimal for your age!")
elif BMI_Formula_Completed >= 65 and age in range(24, 29):
    print("Your BMI is optimal for your age!")
else:
    print("Your BMI is not okay for your age!!!")

	

