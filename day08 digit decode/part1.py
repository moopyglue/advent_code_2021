
print("¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬")

# read in the list of horizontal positions
# and calculate the minimum and maximum
d=0
with open("rawdata") as inputfile:
    for n in inputfile.readlines():
        a = n.strip().split(" | ")
        b = a[1].split()
        l=[]
        # lengths 2,4,3,7 map to digits 1,4,7,8
        # just count total number of those found(d)
        for c in b:
            l.append(len(c))
            if len(c) in [2,4,3,7]: d+=1

print(d)
        
print("¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬")
