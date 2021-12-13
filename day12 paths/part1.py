
import shared

shared.header()

data=shared.infile("rawdata","alphanumlist")

# setup needed data structure
tmap={} ; tdata={}
for n in data:
    if n[0] not in tmap: tmap[n[0]]=[]
    tmap[n[0]].append(n[1])
    if n[1] not in tmap: tmap[n[1]]=[]
    tmap[n[1]].append(n[0])
tdata["map"]=tmap
tdata["path"]=["start"]
tdata["count"]=0

def can_visit(cave,path_so_far):
    if cave.isupper(): return True
    if path_so_far.count(cave)==0: return True
    return False

def walk(tdata):
    
    d="    "*(len(tdata["path"])-1)
    location=tdata["path"][-1]
    if location=="end":
        tdata["count"]+=1
        # print(",".join(tdata["path"]))
        return
    for p in tdata["map"][location]:
        if can_visit(p,tdata["path"]):
            tdata["path"].append(p)
            walk(tdata)
            tdata["path"].pop()

    return
       
walk(tdata)

print(tdata["count"])

shared.footer()
