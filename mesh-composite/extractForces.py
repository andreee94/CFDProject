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
parser.add_argument("-case",  type=str, action='store', dest='case',  help="case", default="")
#parser.add_argument("filename", help="Filename")
parser.add_argument("--save", action="store_true", help="If save to file", default=False)
parser.add_argument("--show", action="store_true", help="If show a figure", default=False)
parser.add_argument('--savepath', type=str, action='store', dest='savepath', help='Path in which to save the figures ending with /', default="") # TODO add a 

params = parser.parse_args()


path_blade0 = params.case + "/postProcessing/forces-blade0/0/forces.dat"
path_blade1 = params.case + "/postProcessing/forces-blade1/0/forces.dat"
path_blade2 = params.case + "/postProcessing/forces-blade2/0/forces.dat"


index_time = 0

index_pressure_fx = 1
index_pressure_fy = 2
index_pressure_fz = 3
index_viscous_fx = 4
index_viscous_fy = 5
index_viscous_fz = 6
index_porous_fx = 7
index_porous_fy = 8
index_porous_fz = 9

index_pressure_Mx = 10
index_pressure_My = 11
index_pressure_Mz = 12
index_viscous_Mx = 13
index_viscous_My = 14
index_viscous_Mz = 15
index_porous_Mx = 16
index_porous_My = 17
index_porous_Mz = 18



def getValues(filename, indexes):
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
            values = [v for i, v in enumerate(values) if i in indexes]
            res.append(values)
    return res
        
        
def saveValues(filename, matrix, forces=False):  #, indexes):
    with open(filename, 'w') as f:
        if forces:
        f.write("# time | Fpx-blade0 | Fpx-blade1 | Fpx-blade2 | Fpx-sum | Ftaux-blade0 | Ftaux-blade1 | Ftaux-blade2 | Ftaux-sum | | Fpy-blade0 | Fpy-blade1 | Fpy-blade2 | Fpy-sum | Ftauy-blade0 | Ftauy-blade1 | Ftauy-blade2 | Ftauy-sum | FX-sum | FY-sum\n")
        else: 
            f.write("# time | Mpz-blade0 | Mpz-blade1 | Mpz-blade2 | Mpz-sum | Mtauz-blade0 | Mtauz-blade1 | Mtauz-blade2 | Mtauz-sum | Mz-sum\n")
        for values in matrix:
            #f.write(' '.join([str(v) for i, v in enumerate(values) if i in indexes]) '\n')
            f.write(' '.join([str(v) for i, v in enumerate(values)]) + '\n')
    
    
def getfloatarrayfromline(line):
    return [float(x) for x in line.split(" ")]
    

def fixLine(line):
    # https://stackoverflow.com/a/1546251
    # this removes "all whitespace characters (space, tab, newline, return, formfeed)"
    line = line.split("#")[0]
    line=line.replace("(", "")
    line=line.replace(")", "")
    # remove comment at the end of the line
    return " ".join(line.split())


def column(matrix, i):
    return [row[i] for row in matrix]


def myplotmomentum(time, Mz, save=False, show=True, filename='Mz-summation', legend=["Mz-sum"], unit='Nm', ylim=[-0.6, 1]):
    fig = plt.figure(num=None, figsize=(10, 8), dpi=80, facecolor='w', edgecolor='k')
    ax = plt.subplot(111)

    plot(time, Mz, 'r-', markersize=1, markeredgewidth=1, markeredgecolor='r', markerfacecolor='None' )
    # plot(time, pFx, 'r-', markersize=1, markeredgewidth=1, markeredgecolor='r', markerfacecolor='None' )
    # plot(time, pFy, 'g-', markersize=1, markeredgewidth=1, markeredgecolor='r', markerfacecolor='None' )
    # plot(time, pFz, 'b-', markersize=1, markeredgewidth=1, markeredgecolor='r', markerfacecolor='None' )

    legendStrings = legend  # ["Mz-sum"]

    box = ax.get_position()
    ax.set_position([box.x0+box.width*0.1, box.y0+box.height*0.05, box.width*0.9, box.height])
    ax.legend(legendStrings, loc='best')
    ax.set_ylim(ylim)  # [-0.6, 1])
    plt.xlabel(r'Time, [s]')
    plt.ylabel(filename + " [" + unit + "]") # r'Momentum Z (summation), [Nm]')

    if save:
        fig.savefig(params.savepath + filename + ".png")
        
    if show:
        plt.show()



## EXTRACT MOMENTUM AND SUM THEM

indexes = [index_time, index_pressure_Mz, index_viscous_Mz]
values_blade0 = getValues(path_blade0, indexes)
values_blade1 = getValues(path_blade1, indexes)
values_blade2 = getValues(path_blade2, indexes)

matrix = []
for j in  range(len(values_blade0)): 
    row = []
    for i in range(len(indexes)):
        if i == 0:  # do not repeat time column
            row.append(values_blade0[j][i])
        else:
            row.append(values_blade0[j][i])
            row.append(values_blade1[j][i])
            row.append(values_blade2[j][i])
            row.append(row[-1] + row[-2] + row[-3]) # summation column of single momentum for 3 blades
    row.append(row[-1] + row[-5]) # summation column of pressure and viscous momentum
    matrix.append(row)

saveValues(params.savepath + "res-momentum.dat", matrix)

time = column(matrix, 0)  # 0 = time index
sumMzp = column(matrix, 4)  # -1 = summation of momentum index
sumMztau = column(matrix, -2)  # -1 = summation of momentum index
sumMz = column(matrix, -1)  # -1 = summation of momentum index

myplotmomentum(time, sumMzp, save=params.save, show=False,  filename='Mz-pressure-summation')
myplotmomentum(time, sumMztau, save=params.save, show=False,  filename='Mz-tau-summation')
myplotmomentum(time, sumMz, save=params.save, show=False,  filename='Mz-summation')



## EXTRACT FORCES AND SUM THEM

indexes = [index_time, index_pressure_fx, index_viscous_fx, index_pressure_fy, index_viscous_fy]
values_blade0 = getValues(path_blade0, indexes)
values_blade1 = getValues(path_blade1, indexes)
values_blade2 = getValues(path_blade2, indexes)

matrix = []
# time || fxp0 fxp1 fxp2 fxp fxtau0 fxtau1 fxtau2 fxtau || fyp0 fyp1 fyp2 fyp fytau0 fytau1 fytau2 fytau || fx fy
for j in  range(len(values_blade0)): 
    row = []
    for i in range(len(indexes)):
        if i == 0:  # do not repeat time column
            row.append(values_blade0[j][i])
        else:
            row.append(values_blade0[j][i])
            row.append(values_blade1[j][i])
            row.append(values_blade2[j][i])
            row.append(row[-1] + row[-2] + row[-3]) # summation column of single forces for 3 blades
    row.append(row[-1-8] + row[-5-8]) # summation column of pressure and viscous momentum
    row.append(row[-1-1] + row[-5-1]) # summation column of pressure and viscous momentum
    matrix.append(row)

saveValues(params.savepath + "res-forces.dat", matrix, forces=True)

time = column(matrix, 0)  # 0 = time index
sumFX = column(matrix, -2)  # -2 = summation of fx index
sumFY = column(matrix, -1)  # -1 = summation of fy index

myplotmomentum(time, sumFX, save=params.save, show=False,  filename='Fx-summation', legend=["Sum of forces X"], unit="N", ylim=[-20, 25])
myplotmomentum(time, sumFY, save=params.save, show=params.show,  filename='Fy-summation', legend=["Sum of forces Y"], unit="N", ylim=[-20, 25])




#from numpy import loadtxt
#lines = loadtxt(filename, comments="#", delimiter=" ", unpack=False)
#time = [float(n) for n in lines[:, 0]]  # 0 = time index
#sumMz = [float(n) for n in lines[:, 4]]  # 4 = summation of momentum index
#return x, y















