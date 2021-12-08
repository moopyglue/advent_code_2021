
print("_"*100)

# convert pattern of letters into nominal binary number
def make_bin(x):
    j=0
    for n in x:
        if n == "a" : j+=1
        if n == "b" : j+=2
        if n == "c" : j+=4
        if n == "d" : j+=8
        if n == "e" : j+=16
        if n == "f" : j+=32
        if n == "g" : j+=64
    return j

# read in the list of horizontal positions
# and calculate the minimum and maximum
d=0
with open("rawdata") as inputfile:
    for line in inputfile.readlines():
        data = line.strip().split(" | ")
        res={}
        for x in data[0].split():
            # first pull out known number based on length for 1,4,7,8
            bin=make_bin(x)
            if len(x) == 2 : res[1]=bin
            if len(x) == 3 : res[7]=bin
            if len(x) == 4 : res[4]=bin
            if len(x) == 7 : res[8]=bin
        for x in data[0].split():
            # looking for len(6) values for 0,6,9 
            # 9 has 4 contained in it
            # 6 has 1 contained in it
            # 0 is remaining len(6)
            bin=make_bin(x)
            if len(x) == 6 :
                if ( bin & res[4] ) == res[4] : res[9] = bin
                elif ( bin & res[1] ) != res[1] : res[6]= bin
                else: res[0] = bin
        for x in data[0].split():
            # looking for len(5) values for 2,3,5 
            # 3 must contain 1
            # 5 must contain the bitwise overlap of 4 & 6
            # 2 is the one not yet identified
            bin=make_bin(x)
            if len(x) == 5 :
                if ( bin & res[1] ) == res[1] : res[3] = bin
                elif ( res[4] & res[6] & bin ) == ( res[4] & res[6] ) : res[5] = bin
                else: res[2] = bin
        # now we have a map for each number we use it to decode
        # the last for digits of each line 
        e=0
        for y in data[1].split():
            for z in res:
                if make_bin(y) == res[z]:
                    e=(e*10)+z
                    break
        # add the 4 digit numbers to the total(d)
        d+=e

print(d)        
        

        
print("¬"*100)
