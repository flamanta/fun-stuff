weight = float(input("Weight in kg? "))
height = float(input("Height in cm? "))

def bmi_calc(weight, height):
    height = height/100
    bmi = round(weight/(height** 2), 1)
    if bmi >= 27.5:
        return "Your BMI is {}, and it is in the high risk range.".format(bmi)
    elif bmi >= 23:
        return "Your BMI is {}, and it is in the moderate risk range.".format(bmi)
    elif bmi >= 18.5:
        return "Your BMI is {}, and it is in the low risk range.".format(bmi)
    else:
        return "Your BMI is {}, and you are at risk of nutritional deficiency diseases and osteoporosis.".format(bmi)

print(bmi_calc(weight, height))