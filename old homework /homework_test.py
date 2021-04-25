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