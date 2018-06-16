import os
import datetime
import time, sys
import argparse

def myround(num, decimals=4, strConversion=True):
    num = round(num, decimals)
    if not strConversion:
        return num
    else:
        return ("{0:." + str(decimals) + "f}").format(num)  # keep trailing zeros

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def formatTimeDelta(now):
    seconds = now.total_seconds()
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    if hours > 0:
        return  str(int(hours)) + " h " + str(int(minutes)) + " min " + str(int(seconds)) + ' s'
    else:
        return  str(int(minutes)) + " min " + str(int(seconds)) + ' s'


def formatTime(now):
    return str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)


parser = argparse.ArgumentParser()
parser.add_argument("-case",  type=str, action='store', dest='case',  help="case", default=".")
parser.add_argument("-pause",  type=int, action='store', dest='pause',  help="case", default=10)
parser.add_argument("-endtime",  type=float, action='store', dest='endtime',  help="case", default=1.8)
#parser.add_argument("filename", help="Filename")
#parser.add_argument("--save", action="store_true", help="If save to file", default=False)
#parser.add_argument("--show", action="store_true", help="If show a figure", default=False)
#parser.add_argument('--savepath', type=str, action='store', dest='savepath', help='Path in which to save the figures ending with /', default="")
params = parser.parse_args()


mainfolder = params.case
pause = params.pause # seconds
endtime = params.endtime

startdate = datetime.datetime.now()

while not os.path.isdir(mainfolder + "/" + str(endtime)):
    maxtime = 0
    for x in os.listdir(mainfolder):
        if isfloat(x):
            maxtime = max(maxtime, float(x))
    perc = 100 * maxtime / endtime
    if perc != 0:
        now = datetime.datetime.now()
        duration = datetime.timedelta(seconds=((now - startdate).seconds/(perc)*100))
        endestimation = startdate + duration
        
        str1 = myround(perc, decimals=2, strConversion=True) + "% completed. "
        str2 = " Running time = " + formatTimeDelta(datetime.datetime.now() - startdate) +  ". "
        str3 = "Total time = " + formatTimeDelta(duration) + ". "
        str4 = ". End estimation = " + formatTime(endestimation) + ". "
        
        print(str1 + str2 + str3 + str4, end="\r")
        #sys.stdout.write("\r" )
        sys.stdout.flush()
    
    time.sleep(pause)
    
print("Completed")
        
        
        
        
        
        
     
