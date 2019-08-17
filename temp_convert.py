# Temperature converter
# https://en.wikipedia.org/wiki/Conversion_of_units_of_temperature

# To implement: calibration table similar to that of on Wikipedia


class tempConvert:
    """Temperature conversion object.

    Converts temperature from one temperature scale to another.

    Available temperature scales are:
    Celsius (C), Kelvin (K), Fahrenheit (F), Rankine (R),
    Delisle (DE), Newton (N), Reaumur (RE), Romer (RO).

    """

    def __init__(self, temp, origScale, newScale):
        """Initializes temperature conversion object."""
        self.temp = temp
        self.origScale = origScale
        self.newScale = newScale
        self.output = None

    def convert(self):
        """Converts the temperature from one scale to another."""

        # Change origScale to upper case + check for input
        try:
            self.origScale = self.origScale.upper()
        except AttributeError:
            print(
                "Please input the correct abbreviations for the temperature scales."
            )
            print("'C' for Celsius, 'K' for Kelvin, 'F' for Fahrenheit,")
            print("'R' for Rankine, 'DE' for Delisle, 'N' for Newton,")
            print("'RE' for Reaumur, 'RO' for Romer")
            return

        # Change newScale to upper case + check for input
        try:
            self.newScale = self.newScale.upper()
        except AttributeError:
            print(
                "Please input the correct abbreviations for the temperature scales."
            )
            print("'C' for Celsius, 'K' for Kelvin, 'F' for Fahrenheit,")
            print("'R' for Rankine, 'DE' for Delisle, 'N' for Newton,")
            print("'RE' for Reaumur, 'RO' for Romer")
            return

        # Put both origScale and newScale together to check if valid
        inp_scales = [self.origScale, self.newScale]

        # Check if origScale and newScale are the same
        if self.origScale == self.newScale:
            print("Please ensure that the two temperature", "scales are different.")
            return

        scales = ["C", "K", "F", "R", "DE", "N", "RE", "RO"]
        scale_check = set(inp_scales).issubset(scales)

        if not scale_check:
            print(
                "Please input the correct abbreviations for the", "temperature scales."
            )
            print("'C' for Celsius, 'K' for Kelvin, 'F' for Fahrenheit,")
            print("'R' for Rankine, 'De' for Delisle, 'N' for Newton,")
            print("'Re' for Reaumur, 'Ro' for Romer")
            return
        else:
            if self.origScale == "C":
                self.output = self.convertC()
            elif self.origScale == "K":
                self.output = self.convertK()
            elif self.origScale == "F":
                self.output = self.convertF()
            elif self.origScale == "R":
                self.output = self.convertR()
            elif self.origScale == "De":
                self.output = self.convertDe()
            elif self.origScale == "N":
                self.output = self.convertN()
            elif self.origScale == "Re":
                self.output = self.convertRe()
            elif self.origScale == "Ro":
                self.output = self.convertRo()

        self.printOut()

    def convertC(self):
        """Converts from Celsius to another temperature scale."""

        if self.newScale == "K":
            output = round(self.temp + 273.15, 2)
            return output
        elif self.newScale == "F":
            output = round(self.temp * 9 / 5 + 32, 2)
            return output
        elif self.newScale == "R":
            output = round((self.temp + 273.15) * 9 / 5, 2)
            return output
        elif self.newScale == "DE":
            output = round((100 - self.temp) * 3 / 2, 2)
            return output
        elif self.newScale == "N":
            output = round(self.temp * 33 / 100, 2)
            return output
        elif self.newScale == "RE":
            output = round(self.temp * 4 / 5, 2)
            return output
        elif self.newScale == "RO":
            output = round(self.temp * 21 / 40 + 7.5, 2)
            return output

    def convertK(self):
        """Converts from Kelvin to another temperature scale."""

        if self.newScale == "C":
            output = round(self.temp - 273.15, 2)
            return output
        elif self.newScale == "F":
            output = round(self.temp * 9 / 5 - 459.67, 2)
            return output
        elif self.newScale == "R":
            output = round(self.temp * 9 / 5, 2)
            return output
        elif self.newScale == "DE":
            output = round((373.15 - self.temp) * 3 / 2, 2)
            return output
        elif self.newScale == "N":
            output = round((self.temp - 273.15) * 33 / 100, 2)
            return output
        elif self.newScale == "RE":
            output = round((self.temp - 273.15) * 4 / 5, 2)
            return output
        elif self.newScale == "RO":
            output = round((self.temp - 273.15) * 21 / 40 + 7.5, 2)
            return output

    def convertF(self):
        """Converts from Fahrenheit to another temperature scale."""

        if self.newScale == "C":
            output = round(5 / 9 * (self.temp - 32), 2)
            return output
        elif self.newScale == "K":
            output = round((self.temp + 459.67) * 5 / 9, 2)
            return output
        elif self.newScale == "R":
            output = round(self.temp + 459.67, 2)
            return output
        elif self.newScale == "DE":
            output = round((212 - self.temp) * 5 / 6, 2)
            return output
        elif self.newScale == "N":
            output = round((self.temp - 32) * 11 / 60, 2)
            return output
        elif self.newScale == "RE":
            output = round((self.temp - 32) * 4 / 9, 2)
            return output
        elif self.newScale == "RO":
            output = round((self.temp - 32) * 7 / 24 + 7.5, 2)
            return output

    def convertR(self):
        """Converts from Rankine to another temperature scale."""

        if self.newScale == "C":
            output = round((self.temp - 491.67) * 5 / 9, 2)
            return output
        elif self.newScale == "F":
            output = round(self.temp - 459.67, 2)
            return output
        elif self.newScale == "K":
            output = round(self.temp * 5 / 9, 2)
            return output
        elif self.newScale == "DE":
            output = round((671.67 - self.temp) * 5 / 6, 2)
            return output
        elif self.newScale == "N":
            output = round((self.temp - 491.67) * 11 / 60, 2)
            return output
        elif self.newScale == "RE":
            output = round((self.temp - 491.67) * 4 / 9, 2)
            return output
        elif self.newScale == "RO":
            output = round((self.temp - 491.67) * 7 / 24 + 7.5, 2)
            return output

    def convertDe(self):
        """Converts from Delisle into another temperature scale."""

        if self.newScale == "C":
            output = round(100 - self.temp * 2 / 3, 2)
            return output
        elif self.newScale == "F":
            output = round(212 - self.temp * 6 / 5, 2)
            return output
        elif self.newScale == "K":
            output = round(373.15 - self.temp * 2 / 3, 2)
            return output
        elif self.newScale == "R":
            output = round(671.67 - self.temp * 6 / 5, 2)
            return output
        elif self.newScale == "N":
            output = round(33 - self.temp * 11 / 50, 2)
            return output
        elif self.newScale == "RE":
            output = round(80 - self.temp * 8 / 15, 2)
            return output
        elif self.newScale == "RO":
            output = round(60 - self.temp * 7 / 20, 2)
            return output

    def convertN(self):
        """Converts from Newton to another temperature scale."""

        if self.newScale == "C":
            output = round(self.temp * 100 / 33, 2)
            return output
        elif self.newScale == "F":
            output = round(self.temp * 60 / 11 + 32, 2)
            return output
        elif self.newScale == "K":
            output = round(self.temp * 100 / 33 + 273.15, 2)
            return output
        elif self.newScale == "R":
            output = round(self.temp * 60 / 11 + 491.67, 2)
            return output
        elif self.newScale == "De":
            output = round((33 - self.temp) * 50 / 11, 2)
            return output
        elif self.newScale == "Re":
            output = round(self.temp * 80 / 33, 2)
            return output
        elif self.newScale == "Ro":
            output = round(self.temp * 35 / 22 + 7.5, 2)
            return output

    def convertRe(self):
        """Converts from Reaumur to another temperature scale."""

        if self.newScale == "C":
            output = round(self.temp * 5 / 4, 2)
            return output
        elif self.newScale == "F":
            output = round(self.temp * 9 / 4 + 32, 2)
            return output
        elif self.newScale == "K":
            output = round(self.temp * 5 / 4 + 273.15, 2)
            return output
        elif self.newScale == "R":
            output = round(self.temp * 9 / 4 + 491.67, 2)
            return output
        elif self.newScale == "DE":
            output = round((80 - self.temp) * 15 / 8, 2)
            return output
        elif self.newScale == "N":
            output = round(self.temp * 33 / 80, 2)
            return output
        elif self.newScale == "RO":
            output = round(self.temp * 21 / 32 + 7.5, 2)
            return output

    def convertRo(self):
        """Convert from Romer into another temperature scale."""

        if self.newScale == "C":
            output = round((self.temp - 7.5) * 40 / 21, 2)
            return output
        elif self.newScale == "F":
            output = round((self.temp - 7.5) * 24 / 7 + 32, 2)
            return output
        elif self.newScale == "K":
            output = round((self.temp - 7.5) * 40 / 21 + 273.15, 2)
            return output
        elif self.newScale == "R":
            output = round((self.temp - 7.5) * 24 / 7 + 491.67, 2)
            return output
        elif self.newScale == "DE":
            output = round((60 - self.temp) * 20 / 7, 2)
            return output
        elif self.newScale == "N":
            output = round((self.temp - 7.5) * 22 / 35, 2)
            return output
        elif self.newScale == "RE":
            output = round((self.temp - 7.5) * 32 / 21, 2)
            return output

    def printOut(self):
        """Prints out the conversion results."""

        print(
            f"{self.temp} {self.origScale} is approximately",
            f"{self.output} {self.newScale}.",
        )
