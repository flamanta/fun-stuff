import numpy as np
import sys
import csv
import matplotlib.pyplot as plt

np.set_printoptions(threshold=sys.maxsize)  # print out arrays fully

# Disable error of plotting too many times
plt.rcParams.update({"figure.max_open_warning": 0})


class Material:
    """Material object."""

    def __init__(self, numMaterials):
        """Initialize the material object."""

        # Number of materials in data sheet
        self.numMaterials = numMaterials

    def files(self):
        """Generate list of strain and stress files."""

        # Create list of strain files in str format
        strainFiles = []
        for num in range(1, self.numMaterials + 1):
            file = "strain" + str(num) + ".csv"
            strainFiles.append(file)
        strainFiles = np.array(strainFiles)

        # Create list of stress files in str format
        stressFiles = []
        for num in range(1, self.numMaterials + 1):
            file = "stress" + str(num) + ".csv"
            stressFiles.append(file)
        stressFiles = np.array(stressFiles)

        return strainFiles, stressFiles

    def strainStress(self):
        """Imports strain and stress from the files.
        Calculates true strain and stress.
        Plots engineering and true stress-strain curves."""

        strainFiles, stressFiles = self.files()

        for num in range(self.numMaterials):

            # Import strain
            strain = np.loadtxt(strainFiles[num])
            strain = strain.T

            # Import stress
            stress = np.loadtxt(stressFiles[num])
            stress = stress.T
            stress = stress / (10 ** 9)

            # Calculate true strain
            Tstrain = np.log(1 + strain)

            # Calculate true stress
            Tstress = stress * (1 + strain)

            # Create figure
            fig = plt.figure()
            ax = fig.add_subplot(111)

            # Plot title
            title = "Stress-strain plot of Material " + str(num + 1)

            # Matplotlib parameters
            plt.title(title)
            plt.xlabel("Strain")
            plt.ylabel("Stress (GPa)")
            plt.grid()

            # Plots and legend
            ax.plot(strain, stress)
            ax.plot(Tstrain, Tstress)
            plt.legend(["Engineering", "True"], loc="lower center")


plt.show()
