
import re

def load_lines (file):
    # load data file into memory
    with open(file) as inputfile:
        # read in the list of bingo balls only(first line) - list of strings
        lines=[]
        for line in inputfile.readlines():
            linelist=[]
            for val in re.split("[^0-9]+",line.strip()):
                linelist.append(int(val))
            lines.append(linelist)
    return lines            

def plot_vent(dic,x,y):
    s = str(x)+","+str(y)
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1

def sign(n):
    if n>0: return 1
    if n<0: return -1
    return 0