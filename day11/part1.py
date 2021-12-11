
import shared

print("¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬")

data=shared.infile("rawdata",style="digitarray")

def print_grid(data,tag=""):
    print(tag)
    for a in range(len(data)):
        for b in range(len(data[a])):
            print("%-3d"%(data[a][b]),end="")
        print("")

# pregenerate a loop array to make 2 dimentional loops easier
looparray=[]
for a in range(len(data)):
    for b in range(len(data[a])):
        looparray.append([a,b])
        
# modifiers for depth 1 flash
modifiers=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

ftot=0
for loop in range(100):
    
    # add 1 to all octopi & track triggered flashes
    flashes=[]
    for (a,b) in looparray:
        data[a][b]+=1
        if data[a][b]==10:
            flashes.append([a,b])
            
    # loop through flashes and triggered flashes 
    # until there are no more flashes
    while len(flashes)!=0:
        newflashes=[]
        for (x,y) in flashes:
            for (a,b) in modifiers:
                if not (x+a<0 or y+b<0 or x+a>=len(data) or y+b>=len(data[0])):
                    data[x+a][y+b]+=1
                    if data[x+a][y+b]==10:
                        newflashes.append([x+a,y+b])
        flashes=newflashes
    
    # everything which is 10 and above has flashed so set back to 0    
    for a in range(len(data)):
        for b in range(len(data[a])):
            if data[a][b] >9 :
                ftot+=1
                data[a][b]=0
    
print_grid(data)
print(ftot)


print("¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬")
