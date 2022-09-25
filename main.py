# Author : Michael Dittman
# Email : dittmanm@msu.edu
# Sparameter grapher for Agilent Field Fox network analyzer
# This isn't the most user friendly, but makes nice plots quickly

import matplotlib.pyplot as plt
import os

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

def graph_sparam(FILENAME, frequency_data, sparam_data, x_axis, y_axis, contains_phase, directory):
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
    if contains_phase:
        plt.scatter(frequency_data, sparam_data)
    else:
        # Plot function better for log mag data
        plt.plot(frequency_data, sparam_data)

    # Save the image
    export_filename = FILENAME.split(".")[0]
    plt.savefig(export_filename)
    #plt.show()
    plt.close()

#FILENAME = "data/lab2/1AS11.csv"

directory = "data/lab2/"

for filename in os.listdir(directory):

    frequency_data, sparam_data = import_data(directory + filename)

    contains_phase = False

    y_axis_name = "" # "$S_{21}$ [dB]"

    s_param_types = ["S11", "S12", "S13", "S21", "S22", "S23", "S31", "S32", "S33"]

    for s_param_type in s_param_types:
        if s_param_type in filename:
            y_axis_name =  "$_{" + s_param_type + "}$"

    if "PHS" in filename:
        contains_phase = True
        y_axis_name = y_axis_name + "[deg]"
    else:
        y_axis_name = y_axis_name + "[dB]"


    graph_sparam(filename, frequency_data, sparam_data, "Frequency [GHz]", y_axis_name, contains_phase, directory)

#print(frequency_data, sparam_data)

