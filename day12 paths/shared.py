import re

# general file input routine to make importing data quicker
# at beinging of each day (maybe :¬)
def infile(filename,style="normal",start=0,end=999999):
    
    result=[]
    with open(filename) as inputfile:
        raw=list(map(lambda x:x.strip(),inputfile.readlines()))

    for (linecount,line) in enumerate(raw):
        
        if linecount<(start-1) or linecount>(end-1): continue
        l=[] 

        if style=="numlist": # everything except digits is a seperator
            for num in re.split("[^0-9]+",line):
                if num!="": l.append(int(num))
        elif style=="alphanumlist": # everything except alphanumerica is a seperator
            for word in re.split("[^0-9a-zA-Z]+",line):
                l.append(word)
        elif style=="digitlist":  # compressed digit list
            for c in range(len(line)):
                l.append(int(line[c]))
        else:
            l=line  # just read line in as is
 
        result.append(l)
    
    # make single dimentional list if only 1 row
    if len(result)==1:
        result=result[0]
            
    return result

def sign(n):
    # missing maths function created here
    if n>0: return 1
    if n<0: return -1
    return 0

def grouplist(data,groupnum):
    newdata=[]
    newline=[]
    count=0
    for row in data:
        count+=1
        newline.extend(row)
        if count == groupnum:
            count=0
            newdata.append(newline)
            newline=[]
    if len(newline)>0:
        newdata.append(newline)
    return newdata

def surroundtable(data,v):
    newdata=[]
    newdata.append([v]*(len(data[0])+2))
    for line in data:
        newdata.append( [v] + line + [v] )
    newdata.append([v]*(len(data[0])+2))
    return newdata

def header():
    print("¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬")

def footer():
    header()

def printtable(data):
    for a in data: print(a)
