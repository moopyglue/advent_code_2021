
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

# calculate only gamma rate as epsilon rate is calculatable from gamma
gamma=0
for a in range(0,binlen):
    gamma*=2
    if bitcount(lines,a) > (len(lines)/2):
        gamma+=1
epsilon=(((2**binlen)-1)-gamma)

# calculate and print result
print(gamma*epsilon)
