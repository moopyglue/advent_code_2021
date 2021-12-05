
import common

file="rawdata"
lines = common.load_lines(file)

vents={}
    
for line in lines:
    
    # x,y set to beinging of line draw
    # xmove,ymove set to the -1,0,+1 depending on direction of line
    x=line[0] ; y=line[1] ;
    xmove=common.sign(line[2]-line[0])
    ymove=common.sign(line[3]-line[1])
    
    # plot line stopping when reach end point
    while (x,y) != (line[2],line[3]):
        common.plot_vent(vents,x,y)
        y+=ymove
        x+=xmove
    common.plot_vent(vents,x,y)
    
# print count of locations where vents where 2+ 
count=0
for key in vents:
    if vents[key] >= 2 : count+=1
print("result=%d" % (count) )
        