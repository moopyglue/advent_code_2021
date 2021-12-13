
import re

def load_lines (file):
    with open(file) as inputfile:
        # convert each line into a list of 4 integers
        lines=[]
        for line in inputfile.readlines():
            linelist=[]
            # split line on any 1+ non-numical(0-9) chars, 
            for val in re.split("[^0-9]+",line.strip()):
                linelist.append(int(val))
            lines.append(linelist)
    return lines            

def plot_vent(dic,x,y):
    # +1 a dictionary element
    s = str(x)+","+str(y)
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1

def sign(n):
    # missing maths function created here
    if n>0: return 1
    if n<0: return -1
    return 0