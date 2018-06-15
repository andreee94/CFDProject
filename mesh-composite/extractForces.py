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
parser.add_argument("--separated", action="store_true", help="If to save each blade", default=False)
parser.add_argument("--save", action="store_true", help="If save to file", default=False)
parser.add_argument("--show", action="store_true", help="If show a figure", default=False)
parser.add_argument('--savepath', type=str, action='store', dest='savepath', help='Path in which to save the figures ending with /', default="") # TODO add a 

params = parser.parse_args()


path_blade0 = params.case + "/postProcessing/forces-blade0/0/forces.dat"
path_blade1 = params.case + "/postProcessing/forces-blade1/0/forces.dat"
path_blade2 = params.case + "/postProcessing/forces-blade2/0/forces.dat"
path_blades = params.case + "/postProcessing/forces-blades/0/forces.dat"


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
        
        
def saveValues(filename, matrix, type=""):  #, indexes):
    with open(filename, 'w') as f:
        if type.lower == "forces":
            if params.separated:
                f.write("# time Fpx-blade0 Fpx-blade1 Fpx-blade2 Fpx-sum Ftaux-blade0 Ftaux-blade1 Ftaux-blade2 Ftaux-sum Fpy-blade0 Fpy-blade1 Fpy-blade2 Fpy-sum Ftauy-blade0 Ftauy-blade1 Ftauy-blade2 Ftauy-sum FX-sum FY-sum\n")
            else:
                f.write("# time Fxp Fxtau Fx Fyp Fytau Fy\n")
        	
        elif type.lower == "momentum":
            if params.separated:
                f.write("# time Mpz-blade0 Mpz-blade1 Mpz-blade2 Mpz-sum Mtauz-blade0 Mtauz-blade1 Mtauz-blade2 Mtauz-sum Mz-sum Power\n")
            else:
                f.write("# time Mpz Mtauz Mz Power\n")
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


def array_multiply(array, coef):
	return [x*coef for x in array]


def column(matrix, i):
    return [row[i] for row in matrix]


def myplot(time, y, legend=None, unit="", show=True,  save=False, filename="", ylim=None, fromTime=0):
    
    if fromTime > 0:
        y = [x for ii, x in enumerate(y) if time[ii] >= fromTime]
        time = [t for t in time if time >= fromTime]
    
    fig = plt.figure(num=None, figsize=(10, 8), dpi=80, facecolor='w', edgecolor='k')
    ax = plt.subplot(111)

    plot(time, y, 'r-', markersize=1, markeredgewidth=1, markeredgecolor='r', markerfacecolor='None' )

    #box = ax.get_position()
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



## EXTRACT MOMENTUM AND SUM THEM

indexes = [index_time, index_pressure_Mz, index_viscous_Mz]
values_blade0 = getValues(path_blade0, indexes)
values_blade1 = getValues(path_blade1, indexes)
values_blade2 = getValues(path_blade2, indexes)
values_blades = getValues(path_blades, indexes)

omega = 2 * math.pi / 60 *  100 # 100 rpm
matrix = []

if params.separated:
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
        row.append(row[-1] * omega)
        matrix.append(row)
    
    saveValues(params.savepath + "res-momentum-separated.dat", matrix, type="momentum")
    
    time = column(matrix, 0)  # 0 = time index
    sumMzp = column(matrix, 4)  # -1 = summation of momentum index
    sumMztau = column(matrix, -3)  # -1 = summation of momentum index
    sumMz = column(matrix, -2)  # -1 = summation of momentum index
    sumPower = column(matrix, -1)  # -1 = summation of power index
    
    
    
else:
    for j in  range(len(values_blades)): 
        row = []
        for i in range(len(indexes)):
            row.append(values_blades[j][i])
            
        row.append(row[-1] + row[-2]) # summation column of p and tau
        row.append(row[-1] * omega) # power
        matrix.append(row)
    
    saveValues(params.savepath + "res-momentum.dat", matrix, type="momentum")
    
    time = column(matrix, 0)  # 0 = time index
    sumMzp = column(matrix, 1)  # -1 = summation of momentum index
    sumMztau = column(matrix, 2)  # -1 = summation of momentum index
    sumMz = column(matrix, 3)  # -1 = summation of momentum index
    sumPower = column(matrix, 4)  # -1 = summation of power index


myplot(time, sumMzp, save=params.save, show=False, filename='Mz-pressure', legend=["Momentum of pressure"], unit="Nm", ylim=[-0.3,-0.7], fromTime=0)
myplot(time, sumMztau,  save=params.save, show=False, filename='Mz-tau', legend=["Momentum of shear stress"], unit="Nm", ylim=None, fromTime=0)
myplot(time, sumMz,  save=params.save, show=False, filename='Mz', legend=["Resultant Momentum"], unit="Nm", ylim=[-0.3,-0.7], fromTime=0)
myplot(time, sumPower, save=params.save, show=False,  filename='InstantPower', legend=["Instantaneous power"], unit="W", ylim=[-3.5, -6.5], fromTime=0)

## CALCULATE MEAN POWER     
sumPower = [x for ii, x in enumerate(sumPower) if time[ii] >= 1.2] # extract with delay 
#sumPower = sumPower[5:]  # remove first unreliable data
meanpower = sum(sumPower) / len(sumPower)
power_text = str(meanpower) + '# mean power [W]'
os.system("echo " + power_text + " > " + params.savepath + "meanpower")



## EXTRACT FORCES AND SUM THEM

indexes = [index_time, index_pressure_fx, index_viscous_fx, index_pressure_fy, index_viscous_fy]
values_blade0 = getValues(path_blade0, indexes)
values_blade1 = getValues(path_blade1, indexes)
values_blade2 = getValues(path_blade2, indexes)
values_blades = getValues(path_blades, indexes)

matrix = []
if params.separated:
    # time |fxp0 fxp1 fxp2 fxp fxtau0 fxtau1 fxtau2 fxtau |fyp0 fyp1 fyp2 fyp fytau0 fytau1 fytau2 fytau |fx fy
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
        row.append(row[-1-8] + row[-5-8]) # summation column of pressure and viscous forces x
        row.append(row[-1-1] + row[-5-1]) # summation column of pressure and viscous forces y
        matrix.append(row) 
        
    saveValues(params.savepath + "res-forces-separated.dat", matrix, type="forces")

else:
    # time |fxp fxtau | fyp fytau |fx fy
    for j in  range(len(values_blades)): 
        row = []
        for i in range(len(indexes)):
            row.append(values_blades[j][i])
            
        row.append(row[1] + row[2]) # summation column of p and tau for x
        row.append(row[-2] + row[-3]) # summation column of p and tau for y
        matrix.append(row)
    
    saveValues(params.savepath + "res-forces.dat", matrix, type="forces")
    
    time = column(matrix, 0)  # 0 = time index
    sumMzp = column(matrix, 1)  # -1 = summation of momentum index
    sumMztau = column(matrix, 2)  # -1 = summation of momentum index
    sumMz = column(matrix, 3)  # -1 = summation of momentum index
    sumPower = column(matrix, 4)  # -1 = summation of power index


time = column(matrix, 0)  # 0 = time index
sumFX = column(matrix, -2)  # -2 = summation of fx index
sumFY = column(matrix, -1)  # -1 = summation of fy index

myplot(time, sumFX, save=params.save, show=False,  filename='Fx', legend=["Forces X"], unit="N", ylim=[-20, 25], fromTime=0)
myplot(time, sumFY, save=params.save, show=params.show,  filename='Fy', legend=["Forces Y"], unit="N", ylim=[-20, 25], fromTime=0)




#from numpy import loadtxt
#lines = loadtxt(filename, comments="#", delimiter=" ", unpack=False)
#time = [float(n) for n in lines[:, 0]]  # 0 = time index
#sumMz = [float(n) for n in lines[:, 4]]  # 4 = summation of momentum index
#return x, y

















