
import shared as s
import pprint

s.header()
filename="rawdata"

data=s.style_list("numlist",s.grep(",",s.in_file(filename)))
folds=s.style_list("alphanumlist",s.grep("fold",s.in_file(filename)))

# fold data
def fold(d,xy,f):
    tmp={} ; result=[]
    # fold each data point along line specified
    # folded temporarily into dict to remove duplicates
    for a in d:
        if xy=="x":
            if a[0] < f:
                tmp[str(a[0])+","+str(a[1])]=True
            if a[0] > f:
                tmp[str( a[0]-((a[0]-f)*2) )+","+str( a[1] )]=True
        if xy=="y": 
            if a[1] < f:
                tmp[str(a[0])+","+str(a[1])]=True
            if a[1] > f:
                tmp[str(a[0])+","+str( a[1]-((a[1]-f)*2) )]=True    
    # convert back from dict to 2 dimentional list
    for i in tmp:
        k=i.split(",")
        result.append( [ int(k[0]) , int(k[1]) ] )
    return result

# print the map
def pmap(data):
    # create a blank filled 2 dimentional list(oo)
    xmax=0 ; ymax=0
    for n in data:
        if n[1]>xmax: xmax=n[1]
        if n[0]>ymax: ymax=n[0]
    map=[]
    for x in range(xmax+1):
        mapline=[]
        for y in range(ymax+1):
            mapline.append(" ")
        map.append(mapline)
    # populate list with data points and print
    for a in data:
        map[a[1]][a[0]]='#'
    for x in map:
        print("".join(x))

# apply all folds and print result(pmap)
for f in folds:
    data=fold(data,f[2],int(f[3]))
pmap(data)

s.footer()
