# generally this code probbaly does not make sense unless you
# read this days problem statement, which truthfully is somewhat
# of a bag of spanners (see dodgeball movie training technique)

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

# below see the use of the list(filter(lambda...exit

# filter() presents a subset of an array, based on a python
# lambda function which is wrapped in a list() to covert 
# back to an array.

# filter down the oxygen result
filterlines=lines.copy()
for a in range(0,binlen):
    filtervalue="0"
    if (bitcount(filterlines,a)*2)-len(filterlines) >= 0 :
        filtervalue="1"
    if len(filterlines)>1:
        filterlines=list(filter(lambda p: p[a] == filtervalue,filterlines))
oxyres=int(filterlines[0],2)

# filter down the co2 result
filterlines=lines.copy()
for a in range(0,binlen):
    filtervalue="1"
    if (bitcount(filterlines,a)*2)-len(filterlines) >= 0 :
        filtervalue="0"
    if len(filterlines)>1:
        filterlines=list(filter(lambda p:p[a] == filtervalue,filterlines))
co2res=int(filterlines[0],2)

# print result
print(oxyres*co2res)
