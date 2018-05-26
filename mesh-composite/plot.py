import matplotlib.pyplot as plt
import numpy
import sys
import os.path
from pprint import pprint
import math
import argparse


def pareto_frontier(Xs, Ys, maxX = True, maxY = True):
    # Sort the list in either ascending or descending order of X
    myList = sorted([[Xs[i], Ys[i]] for i in range(len(Xs))], reverse=maxX)
    # Start the Pareto frontier with the first value in the sorted list
    p_front = [myList[0]]    
    # Loop through the sorted list
    for pair in myList[1:]:
        if maxY: 
            if pair[1] >= p_front[-1][1]: # Look for higher values of Y
                p_front.append(pair) # and add them to the Pareto frontier
        else:
            if pair[1] <= p_front[-1][1]: # Look for lower values of Y
                p_front.append(pair) #  and add them to the Pareto frontier
    # Turn resulting pairs back into a list of Xs and Ys
    p_frontX = [pair[0] for pair in p_front]
    p_frontY = [pair[1] for pair in p_front]
    return p_frontX, p_frontY


parser = argparse.ArgumentParser()
parser.add_argument("filename", help="Filename")
parser.add_argument('-x', type=int, action='store', dest='x_index', help='Column index of x starting from 1')
parser.add_argument('-y', type=int, action='store', dest='y_index', help='Column index of y starting from 1')
parser.add_argument('-c', type=int, action='store', dest='c_index', help='Column index of constraint starting from 1', default=None)
parser.add_argument("-xs", "--xsort", action="store_true", help="Sort x vector")
parser.add_argument("--max", action="store_true", help="Take max of y up to now")
parser.add_argument("--min", action="store_true", help="Take min of y up to now")
parser.add_argument("--abs", action="store_true", help="Take abs of y")
parser.add_argument('--update', type=float, action='store', dest='update_time', help='Comumn index of y starting from 1')
parser.add_argument("--xlog", action="store_true", help="Axis x logarithmic")
parser.add_argument("--ylog", action="store_true", help="Axis y logarithmic")
parser.add_argument("--loglog", action="store_true", help="Axis x and y logarithmic")
parser.add_argument("--point", action="store_true", help="Point instead of lines", default=False)
parser.add_argument("--hideC", action="store_true", help="Hide points that does not satisfy the constraint boundary instead of mark in red", default=False)
parser.add_argument('--lowerC', type=float, action='store', dest='lowerConstraint', help='Lower constraint', default=float('-inf'))
parser.add_argument('--upperC', type=float, action='store', dest='upperConstraint', help='Upper constraint', default=0)
parser.add_argument("--pareto", action="store_true", help="Plot pareto frontier, default is maxX and maxY")
parser.add_argument("--paretominX", action="store_true", help="Pareto rule for x", default=False)
parser.add_argument("--paretominY", action="store_true", help="Pareto rule for y", default=False)
params = parser.parse_args()
print(params)

if params.x_index == None or params.y_index == None:
    print('-x, -y parameters are mandatory.')
else:
    x_index = params.x_index - 1
    y_index = params.y_index - 1
    
    plt.show()
    first = True

    while first or params.update_time != None: # always true if update is set
        first = False
        try:
            if params.c_index != None:
                c_index = params.c_index - 1
                data = numpy.loadtxt(params.filename, skiprows=1, usecols=(x_index, y_index, c_index))
            else: data = numpy.loadtxt(params.filename, skiprows=1, usecols=(x_index, y_index))
            #print(data)
            x = data[:, 0]
            y = data[:, 1]
            x_fail, y_fail = [], []
            
            ##################################################
            if params.c_index != None:
                c = data[:, 2]
                x_new, y_new = [], []
                for i, cc in enumerate(c):
                    if cc >= params.lowerConstraint and cc <= params.upperConstraint:
                        x_new.append(x[i])
                        y_new.append(y[i])
                    elif not params.hideC:
                        x_fail.append(x[i])
                        y_fail.append(y[i])
                x = x_new
                y = y_new
                
                #x_new = [x[i] for cc, i in enumerate(params.c) if cc >= params.lowerConstraint and cc <= params.upperConstraint]
                #y_new = [y[i] for cc, i in enumerate(params.c) if cc >= params.lowerConstraint and cc <= params.upperConstraint]
            
            ##################################################
            if params.xsort:
                x.sort()
            ##################################################
            if params.abs:
                y = abs(y)
            ##################################################
            if params.max or params.min:
                y_new = [0] * len(y)
                y_new[0] = y[0] #first item is y[0] in any case
                print(len(y_new))
                for i in range(1,len(y)):
                    if params.max:
                        y_new[i] = max(y[0:i])
                    elif params.min:
                        y_new[i] = min(y[0:i])
                y = y_new
            ##################################################
            if params.xlog or params.loglog:
                plt.xscale('log')
            if params.ylog or params.loglog:
                plt.yscale('log')
            ##################################################
            if params.point:
                if params.c_index != None and not params.hideC:
                    plt.plot(x_fail, y_fail, 'r*')
                plt.plot(x, y, '*')
            else: 
                plt.plot(x, y)
                if params.c_index != None and not params.hideC:
                    plt.plot(x_fail, y_fail, 'r')
            ##################################################
            if params.pareto:
                paretoX, paretoY = pareto_frontier(x, y, maxX=not params.paretominX, maxY=not params.paretominY)
                plt.plot(paretoX, paretoY, 'k--', linewidth=2)
            plt.grid()
        except Exception as e:
            print('Error extracting columns')
            print(e)
        plt.pause(params.update_time)
plt.clf()
