from matplotlib import rc
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
import scipy as sp
from scipy.interpolate import interp1d
import os
import string
import re
import math
from operator import itemgetter
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-case", type=str, action='store', dest='case', help="case", default="")
# parser.add_argument("filename", help="Filename")
parser.add_argument("--separated", action="store_true", help="If to save each blade", default=False)
parser.add_argument("--save", action="store_true", help="If save to file", default=False)
parser.add_argument("--show", action="store_true", help="If show a figure", default=False)
parser.add_argument('--savepath', type=str, action='store', dest='savepath', help='Path in which to save the figures ending with /', default="")  # TODO add a

params = parser.parse_args()

folder = params.case + '/postProcessing/singleGraph/'
folder_times = ['1.8', '2.1', '2.4']
file_inlet = 'line-inlet_nut.xy'
file_outlet = 'line-outlet_nut.xy'

def getValues(filename, indexes=[0, 1]):
    res = []
    with open(filename, 'r') as f:
        lines = f.readlines()

        for line in lines:
            line = fixLine(line)
            if line.startswith('#'):  # comment line
                continue
            if len(line) == 0:  # empty line
                continue
            values = getfloatarrayfromline(line)
            extractedValues = []
            #for ind in indexes:
            #    extractedValues.append(values[ind])
            values = [values[ind] for ind in indexes]
            #values = [v for iii, v in enumerate(values) if iii in indexes]
            res.append(values)
    return res


def getfloatarrayfromline(line):
    return [float(x) for x in line.split(" ")]


def fixLine(line):
    # https://stackoverflow.com/a/1546251
    # this removes "all whitespace characters (space, tab, newline, return, formfeed)"
    line = line.split("#")[0]
    line = line.replace("(", "")
    line = line.replace(")", "")
    # remove comment at the end of the line
    return " ".join(line.split())


def array_multiply(array, coef):
    return [x * coef for x in array]


def array_difference(array1, array2):
    return [array1[ii] - array2[ii] for ii in range(len(array1))]


def array_square(array, power=2):
    return [a**power for a in array]


def column(matrix, i):
    return [row[i] for row in matrix]


values=[] # list of tuples (y, nut)  # where nut is difference between out and in
for t in folder_times:
    filename_inlet = folder + t + '/' + file_inlet
    filename_outlet = folder + t + '/' + file_outlet
    
    v_inlet = getValues(filename_inlet)
    v_outlet = getValues(filename_outlet)
    
    y = column(v_inlet, 0)
    nut = array_difference(column(v_outlet, 1),  column(v_inlet, 1))
    
    values.append((y, nut))


# extract nut column for each time and make sqrt(sum(item^2))
values_single = [sqrt(sum(array_square(values[ii][1]))) for ii in range(len(folder_times))]

avgnut = sum(values_single) / float(len(values_single))

nut_text = str(avgnut) + ' # average nut all times'
os.system("echo '" + nut_text + "' > " + params.savepath + "meannut")

for ii, t in enumerate(folder_times):
    nut_text = str(values_single[ii]) + ' # average nut at time ' + t + ' s'
    os.system("echo '" + nut_text + "' >> " + params.savepath + "meannut")
    


# myplot(time, sumFY, save=params.save, show=params.show, filename='Fy', legend=["Forces Y"], unit="N", ylim=[-20, 25], fromTime=0)



def myplot(time, y, legend=None, unit="", show=True, save=False, filename="", ylim=None, fromTime=0):
    if fromTime > 0:
        y = [x for ii, x in enumerate(y) if time[ii] >= fromTime]
        time = [t for t in time if time >= fromTime]

    fig = plt.figure(num=None, figsize=(10, 8), dpi=80, facecolor='w', edgecolor='k')
    ax = plt.subplot(111)

    plot(time, y, 'r-', markersize=1, markeredgewidth=1, markeredgecolor='r', markerfacecolor='None')

    # box = ax.get_position()
    # ax.set_position([box.x0+box.width*0.1, box.y0+box.height*0.05, box.width*0.9, box.height])
    if legend != None:
        ax.legend(legend, loc='best')

    if ylim != None:
        ax.set_ylim(ylim)

    plt.xlabel(r'Time, [s]')
    plt.ylabel(filename + " [" + unit + "]")

    if save:
        fig.savefig(params.savepath + filename + ".png")

    if show:
        plt.show()
