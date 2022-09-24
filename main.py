# Author : Michael Dittman
# Email : dittmanm@msu.edu
# Sparameter grapher for Agilent Field Fox network analyzer
# This isn't the most user friendly, but makes nice plots quickly

import matplotlib.pyplot as plt

def import_data(filename):
    """
    Import data from the given filename
    :param filename:
    :return:
    """

    # Open the file
    fp = open(filename)

    frequency_data = []
    sparam_data = []

    # Take data?
    take_data = False

    # Iterate over each line
    for line in fp:

        # Split into array
        temp = line.split()

        if take_data == True and temp[0] != "END":
            frequency, sparam = temp[0].split(',')
            frequency_data.append(float(frequency))
            sparam_data.append(float(sparam))

        if temp[0] == "BEGIN":
            take_data = True

    return frequency_data, sparam_data

def graph_sparam(FILENAME, frequency_data, sparam_data, x_axis, y_axis):
    """
    Graph sparameter data
    :param frequency_data:
    :param sparam_data:
    :return:
    """

    fig, axs = plt.subplots(1)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)

    axs.ticklabel_format(axis='x', scilimits=(9, 9))
    axs.set_ylabel(y_axis, fontsize=10)
    axs.set_xlabel(x_axis, fontsize=10)

    # Scatter is better for phase data
    plt.scatter(frequency_data, sparam_data)

    # Plot function better for log mag data
    #plt.plot(frequency_data, sparam_data)

    # Save the image
    export_filename = FILENAME.split(".")[0]
    plt.savefig(export_filename)
    plt.show()

FILENAME = "data/lab1/PHS21.csv"

frequency_data, sparam_data = import_data(FILENAME)

graph_sparam(FILENAME, frequency_data, sparam_data, "Frequency [GHz]", "$S_{21}$ [deg]")

#print(frequency_data, sparam_data)

