import os
import datetime
import time, sys
import argparse
import curses

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


def delLastLine(n=1):
    for _ in range(n):
        sys.stdout.write("\033[F") #back to previous line
        sys.stdout.write("\033[K") #clear line
    
    
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

# start manage cursor
#stdscr = curses.initscr()
#curses.echo()
##curses.nocbreak()
#curses.noecho()
#curses.cbreak()

print("")
print("")

startTime = 0
for x in os.listdir(mainfolder):
    if isfloat(x):
        startTime = max(startTime, float(x))

first = True
while not os.path.isdir(mainfolder + "/" + str(endtime)):
    maxtime = 0
    for x in os.listdir(mainfolder):
        if isfloat(x):
            maxtime = max(maxtime, float(x))
    percTotal = 100 * maxtime / endtime
    percResume = 100 * (maxtime - startTime) / endtime
    if percResume != 0:
        now = datetime.datetime.now()
        duration = datetime.timedelta(seconds=((now - startdate).seconds/(percResume)*100))
        missing = duration - (datetime.datetime.now() - startdate)
        endestimation = startdate + duration
        
        str0 = 'Started at = ' + formatTime(startdate) + '. '
        str1 = myround(percTotal, decimals=2, strConversion=True) + "% completed. "
        str2 = "Running time = " + formatTimeDelta(datetime.datetime.now() - startdate) +  ". "
        str3 = "Total time = " + formatTimeDelta(duration) + ". "
        str4 = "Missing time= " + formatTimeDelta(missing) + ". "
        str5 = "Ending at = " + formatTime(endestimation) + ". "
        
        #stdscr.addstr(0, 0, str1)
        #stdscr.addstr(1, 0, str2)
        #stdscr.addstr(2, 0, str3)
        #stdscr.addstr(3, 0, str4)
        #stdscr.addstr(4, 0, str5)
        #stdscr.refresh()
        
        if not first:
            delLastLine(n=6)
        
        print(str0)
        print(str1)
        print(str2)
        print(str3)
        print(str4)
        print(str5)
        
        ## Python 3 no cursor version
        #sys.stdout.write("\033[F") #back to previous line
        #sys.stdout.write("\033[K") #clear line
        #print("\r" + str1 + str2 + str3 + str4 + str5) #, end="\r")
        ## alternative
        #print("\r" + str1 + str2 + str3 + str4 + str5, end="\r")
        sys.stdout.flush()
        first = False
        ###################################
    
    time.sleep(pause)
    
# stop manage cursor
#curses.echo()
#curses.nocbreak()
#curses.endwin()

print("Completed")
        
        
        
        
        
        
     
