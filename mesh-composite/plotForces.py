#!/usr/bin/python

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
parser.add_argument("folder", help="Folder")
parser.add_argument("filename", help="Filename")
parser.add_argument("--save", action="store_true", help="If save to file", default=False)
parser.add_argument("--show", action="store_true", help="If show a figure", default=False)
parser.add_argument('--savepath', type=str, action='store', dest='savepath', help='Path in which to save the figures ending with /', default="") # TODO add a check on this 

#parser.add_argument('-x', type=int, action='store', dest='x_index', help='Column index of x starting from 1')
#parser.add_argument('-y', type=int, action='store', dest='y_index', help='Column index of y starting from 1')
#parser.add_argument('-c', type=int, action='store', dest='c_index', help='Column index of constraint starting from 1', default=None)
#parser.add_argument("-xs", "--xsort", action="store_true", help="Sort x vector")
#parser.add_argument("--max", action="store_true", help="Take max of y up to now")
#parser.add_argument("--min", action="store_true", help="Take min of y up to now")
#parser.add_argument("--abs", action="store_true", help="Take abs of y")
#parser.add_argument('--update', type=float, action='store', dest='update_time', help='Comumn index of y starting from 1')
#parser.add_argument("--xlog", action="store_true", help="Axis x logarithmic")
#parser.add_argument("--ylog", action="store_true", help="Axis y logarithmic")
#parser.add_argument("--loglog", action="store_true", help="Axis x and y logarithmic")
#parser.add_argument("--point", action="store_true", help="Point instead of lines", default=False)
#parser.add_argument("--hideC", action="store_true", help="Hide points that does not satisfy the constraint boundary instead of mark in red", default=False)
#parser.add_argument('--lowerC', type=float, action='store', dest='lowerConstraint', help='Lower constraint', default=float('-inf'))
#parser.add_argument('--upperC', type=float, action='store', dest='upperConstraint', help='Upper constraint', default=0)
#parser.add_argument("--pareto", action="store_true", help="Plot pareto frontier, default is maxX and maxY")
#parser.add_argument("--paretominX", action="store_true", help="Pareto rule for x", default=False)
#parser.add_argument("--paretominY", action="store_true", help="Pareto rule for y", default=False)
params = parser.parse_args()


graphPath  = "./"

#rc('font',**{'family':'serif','serif':['times']})
#rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('font', size=16.0)
rc('text', usetex=False)
rc('axes', titlesize = 16.0)
rc('axes', labelsize = 16.0)
rc('ytick', labelsize = 16.0)
rc('xtick', labelsize = 16.0)
rc('legend', fontsize = 16.0)

col1 = ['bo-', 'ro-', 'go-', 'co-', 'mo-', 'yo-', 'ko-', 'bs-', 'rs-', 'gs-', 'cs-', 'ms-', 'ys-', 'ks-']


pi = math.pi

###############################################################################

# Group plots:
pltGroup = 0

###############################################################################

### Forces: read 'fan' files ###

table = []
first="true"
index = 0
time = []
pFx = []
pFy = []
pFz = []
pMx = []
pMy = []
pMz = []

if not params.folder.endswith("/"):
    params.folder = params.folder + "/"

for dir in os.listdir(params.folder + params.filename):
    for file in os.listdir(params.folder + params.filename + "/"+dir+"/"):

        fi = open(params.folder + params.filename + "/"+dir+"/"+file)
       
        index = 0

        for s in fi.readlines():
            values = re.split(r'[,()\t\n ]+', s)        
            if values[0] != "#":
                values.remove("")
                for v in range(len(values)):
                    values[v]=float(values[v])

                table.append(values)

        fi.close() 


tup=tuple(table)
sorV=sorted(tup, key=itemgetter(0))

for i in range(len(sorV)):
    time.append(float(sorV[i][0]))
    pFx.append(float(sorV[i][1]))
    pFy.append(float(sorV[i][2]))
    pFz.append(float(sorV[i][3]))
    pMx.append(float(sorV[i][10]))
    pMy.append(float(sorV[i][11]))
    pMz.append(float(sorV[i][12]))

# Plot: Forces

if (pltGroup == 1):
    ax = plt.subplot(223)
    plt.subplots_adjust(left=None, bottom=None, right=None, top=0.87, wspace=0.6, hspace=0.4)
elif (pltGroup == 0):
    fig = plt.figure(num=None, figsize=(10, 8), dpi=80, facecolor='w', edgecolor='k')
    ax = plt.subplot(111)

plot(time, pFx, 'r-', markersize=1, markeredgewidth=1, markeredgecolor='r', markerfacecolor='None' )
plot(time, pFy, 'g-', markersize=1, markeredgewidth=1, markeredgecolor='r', markerfacecolor='None' )
plot(time, pFz, 'b-', markersize=1, markeredgewidth=1, markeredgecolor='r', markerfacecolor='None' )

legendStrings = ["Fx - pressure", "Fy - pressure", "Fz - pressure"]

box = ax.get_position()
ax.set_position([box.x0+box.width*0.1, box.y0+box.height*0.05, box.width*0.9, box.height])
ax.legend(legendStrings, loc='best')
ax.set_ylim(-20, 25)
plt.xlabel(r'Time \, [s]')
plt.ylabel(r'Forces \, [N]')

if params.save:
    fig.savefig(params.savepath + params.filename + '-FORCES.png')



# Plot: Momentum

if (pltGroup == 1):
    ax = plt.subplot(224)
    plt.subplots_adjust(left=None, bottom=None, right=None, top=0.87, wspace=0.6, hspace=0.4)
elif (pltGroup == 0):
    fig = plt.figure(num=None, figsize=(10, 8), dpi=80, facecolor='w', edgecolor='k')
    ax = plt.subplot(111)

plot(time, pMx, 'r-', markersize=1, markeredgewidth=1, markeredgecolor='r', markerfacecolor='None' )
plot(time, pMy, 'g-', markersize=1, markeredgewidth=1, markeredgecolor='r', markerfacecolor='None' )
plot(time, pMz, 'b-', markersize=1, markeredgewidth=1, markeredgecolor='r', markerfacecolor='None' )


legendStrings = ["Mx - pressure", "My - pressure", "Mz - pressure"]

box = ax.get_position()
ax.set_position([box.x0+box.width*0.1, box.y0+box.height*0.05, box.width*0.9, box.height])
ax.legend(legendStrings, loc='best')
ax.set_ylim(-0.8, 1)
plt.xlabel(r'Time \, [s]')
plt.ylabel(r'Momentum \, [Nm]')

if params.save:
    fig.savefig(params.savepath + params.filename + '-MOMENTUM.png')

if params.show:
    plt.show()
