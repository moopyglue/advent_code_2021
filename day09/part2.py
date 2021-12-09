
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

# use structure created(floor[][]) to identify low points
# (lowpoints[][])
lowpoints=[]
for a in range(1,len(floor[0])-1):
    for b in range(1,len(floor)-1):
        if floor[b][a]<floor[b+1][a] and floor[b][a]<floor[b][a+1] and floor[b][a]<floor[b-1][a] and floor[b][a]<floor[b][a-1] :
            lowpoints.append( [b,a,floor[b][a]] )

# define a recirsie function that will count a point given,
# set it to 10 (no longer countable), and then run itself again for 
# 4 surrounding locations
def lp_size(x,y):
    if floor[x][y]>=9:
        return(0)
    floor[x][y]=10
    return(1 + lp_size(x+1,y) + lp_size(x,y+1) + lp_size(x-1,y) + lp_size(x,y-1))

# loop through lowpoints using above recursive finction to generate a list
# of basin sizes (basin_sizes[])
basin_sizes=[]  
for l in lowpoints:
    basin_sizes.append( lp_size(l[0],l[1]) )         

# results as per requested calculation (largest 3 basins)
print(basin_sizes)
basin_sizes.sort(reverse=True)
print(basin_sizes[0],basin_sizes[1],basin_sizes[2])
print(basin_sizes[0]*basin_sizes[1]*basin_sizes[2])
    
print("¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬")
