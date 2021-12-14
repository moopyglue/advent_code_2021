
import shared as s

s.header()
filename="rawdata" ; maxdepth=10

# generate data structures from file
seq=s.style_list("normal",s.in_file(filename,end=1))
map=s.style_list("dictpairs",s.grep(" -> ",s.in_file(filename)))

#-----------------------------
# map(above), empty, and cache are globals

# empty counter array creation
empty={}
for a in map:
    if a not in empty: empty[map[a]]=0

# to avoid exponsential iterations we have to cache so
# that we can shortcust the calculation where possible
cache=[]
for n in range(maxdepth+1):
    cache.append({})

#-----------------------------

# recursive expander uses leveled cache to speed up processing
def expand(seq,depth):

    global map,empty,cache
    
    # skip expansion if cahced value exists
    if seq in cache[depth]:
        return(cache[depth][seq])

    # as no cached value count all vals recursively
    totals=empty.copy()
    for n in range(len(seq)-1): # loop for when seq is > 2 length
        
        pair=seq[n:n+2]
        trio=seq[n]+map[pair]+seq[n+1]
        
        # reached the final expand level
        if depth == 0:
            totals[pair[0]]+=1
            totals[pair[1]]+=1
            break

        # run expand recursively adding totals(totals)
        # for the 2 sides of the trio so for ABC expnads for AB and BC
        # then to avoid middle letter beng counted twice we -1 B
        for qkey,qvalue in expand(trio[0:2],depth-1).items():
            totals[qkey]+=qvalue
        for qkey,qvalue in expand(trio[1:3],depth-1).items():
            totals[qkey]+=qvalue
        totals[map[pair]]-=1
        
    cache[depth][seq]=totals.copy()
    return(totals)
    
final=expand(seq,maxdepth)

#-----------------------------

# print result
print(final)
print("result =",max(final.values())-min(final.values()))

s.footer()
