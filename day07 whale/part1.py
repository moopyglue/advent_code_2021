
print("_"*100)

# read in the list of horizontal positions
# and calculate the minimum and maximum
hozpos=[] 
with open("rawdata") as inputfile:
    for n in inputfile.readline().strip().split(","):
        hozpos.append(int(n))
hozpos.sort()
minpos=hozpos[0]
maxpos=hozpos[len(hozpos)-1]

costs=[]
# loop through each possible final position and calculate
# a cost for moving all crabs to that position 
for x in range(minpos,maxpos):
    fuelcost=0
    for crabsub in hozpos:
        # calculate fuel cost for that number of moves
        fuelcost += abs(crabsub-x)
    costs.append(fuelcost)

# sort the list of costs to find the cheapest
costs.sort()
print("result =",costs[0])

print("¬"*100)
