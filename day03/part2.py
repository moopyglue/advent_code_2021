binlen=12

# function to do single column bitcount
def bitcount(lines,bit):
    y=0
    for line in lines:
        if line[bit] == "1": y+=1
    return y

# read in the data file
with open('rawdata') as inputfile:
    lines = inputfile.readlines()

# filter down the oxygen result
filterlines=lines.copy()
for a in range(0,binlen):
    ind="0"
    if (bitcount(filterlines,a)*2)-len(filterlines) >= 0 : ind="1"
    if len(filterlines)>1: filterlines=list(filter(lambda p: p[a] == ind,filterlines))
oxyres=int(filterlines[0],2)

# filter down the co2 result
filterlines=lines.copy()
for a in range(0,binlen):
    ind="1"
    if (bitcount(filterlines,a)*2)-len(filterlines) >= 0 : ind="0"
    if len(filterlines)>1: filterlines=list(filter(lambda p: p[a] == ind,filterlines))
co2res=int(filterlines[0],2)

# print result
print(oxyres*co2res)