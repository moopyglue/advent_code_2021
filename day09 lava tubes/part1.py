
print("¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬")

# read in input file
with open("rawdata") as inputfile:
    floorraw=inputfile.readlines()

# we create a 2 dimentional array of the numbers 
# with a buffer row/column on each side where value is 10
# this enable simpler testing for low points in the code
floor=[[10]*(len(floorraw[0])+1)]
for a in floorraw:
    line=[10]
    for b in range(len(floorraw[0])-1):
        line.append(int(a[b]))
    line.append(10)
    floor.append(line)
floor.append([10]*(len(floorraw[0])+1))
    
# use structure created(floor[][]) to identify and
# sum the low points
total=0
for a in range(1,len(floor[0])-1):
    for b in range(1,len(floor)-1):
        if ( floor[b][a]<floor[b+1][a] and floor[b][a]<floor[b][a+1] and
             floor[b][a]<floor[b-1][a] and floor[b][a]<floor[b][a-1] ) :
                total+=floor[b][a]+1
               
print(total)
    
print("¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬")
