def bmi_calc(system = 'metric'):
    if system == 'metric':
        try:
            kg = float(input("Weight in kg? "))
        except ValueError:
            return 'Wrong input type for weight in kg. Please input a float.'
        try:
            cm = float(input("Height in cm? "))
        except ValueError:
            return 'Wrong input type for height in cm. Please input a float.'
        m = cm/100
        bmi = round(kg/(m** 2), 1)
    elif system == 'imperial':
        try:
            lb = float(input("Weight in lb? "))
        except ValueError:
            return 'Wrong input for weight in lb. Please input a float.'
        try:
            inch = float(input("Height in inches? "))
        except ValueError:
            return 'Wrong input for height in inches. Please input a float.'
        bmi = round(lb/(inch)**2*703, 1)    
    if bmi >= 27.5:
        return "Your BMI is {}, and it is in the high risk range.".format(bmi)
    elif bmi >= 23:
        return "Your BMI is {}, and it is in the moderate risk range.".format(bmi)
    elif bmi >= 18.5:
        return "Your BMI is {}, and it is in the low risk range.".format(bmi)
    else:
        return "Your BMI is {}, and you are at risk of nutritional deficiency diseases and osteoporosis.".format(bmi)

print(bmi_calc())

# To be rewritten as a class