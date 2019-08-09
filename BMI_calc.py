class bmi_calc():
    '''BMI calculator object, which calculates in both metric and imperial units.

    Weight and height should be input as a float, units is input as a string 
    ('metric' for metric/SI units, 'imperial' for imperial units)

    Default metric units: kg (weight), cm (height)
    Default imperial units: lb (weight), in (height).'''

    def __init__(self, weight, height, units):
        '''Initialize BMI calculator object, with weight, height and system of units.'''

        self.weight = weight
        self.height = height
        self.units = units

    def calc(self):
        '''Computes and prints out to stdout the user's BMI and health advice.'''

        # Check if units is in correct format
        if self.units == 'metric':
            try:
                m = self.height/100
                bmi = round(self.weight/(m ** 2), 1)
                self.print_calc(bmi)
            except TypeError:
                print('Wrong input for either height or weight. Please input a number.')

        elif self.units == 'imperial':
            try:
                bmi = round(self.weight/(self.height)**2*703, 1)
                self.print_calc(bmi)
            except TypeError:
                print('Wrong input for either height or weight. Please input a number.')

        else:
            print(
                "Wrong input for units. Use 'metric' for metric/SI units or 'imperial' for imperial units.")

    def print_calc(self, bmi):
        '''Prints out to stdout the user's BMI and health advice.'''

        if bmi >= 27.5:
            print(f'Your BMI is {bmi}, and it is in the high risk range.')
        elif bmi >= 23:
            print(f'Your BMI is {bmi}, and it is in the moderate risk range.')
        elif bmi >= 18.5:
            print(f'Your BMI is {bmi}, and it is in the low risk range.')
        else:
            print(f'Your BMI is {bmi}, and you are at risk of nutritional deficiency diseases and osteoporosis.')
