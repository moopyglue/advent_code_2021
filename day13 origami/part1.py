
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

# run first fold and print remaining dots
data=fold(data,folds[0][2],int(folds[0][3]))
print(len(data))

s.footer()
