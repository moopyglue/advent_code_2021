
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

# calculate only gamma rate
# epsilon rate is derived later from gamma and binlen
gamma=0
for a in range(0,binlen):
    gamma*=2   # double result every digit to convert automagically from binary to decimal
    if bitcount(lines,a) > (len(lines)/2): gamma+=1

# calculate and print result
epsilon=(((2**binlen)-1)-gamma)
print(gamma*epsilon)
