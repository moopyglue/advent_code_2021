#!/usr/bin/python3

import re
import sys
from pprint import pprint
from shared import style_list,in_file,grep,separator,printtable
from time import time

def main():
    
    tt=time()

    raw=in_file("rawdata")
    data=[]
    for line in raw:
        if len(line)<5: continue
        elif line.find("scanner")>0:
            scanner=int(line.split(" ")[2])
            data.append( { "id":scanner , "scanner":[], "diff":[0,0,0] } )
        else:
            l=line.split(",")
            data[scanner]["scanner"].append( [int(l[0]),int(l[1]),int(l[2])] )
    
    # for a in range(len(data)):
    #     data[a]["vers"]=generate_scanner_orientations(data[a]["scanner"])

    print("#1 -",time()-tt,file=sys.stderr)

    totest=set()
    totest.add(0)

    data[0]["found"]=data[0]["scanner"]

    while len(totest)>0:
        for a in list(totest):
            print("==========================",a,"%3.3fs"%(time()-tt))
            for b in range(len(data)):
                if "found" in data[b]: continue
                # print("testing",a,b)
                if scanner_overlap(data[a],data[b]):
                    print(b,data[b]["diff"])
                    totest.add(b)
                # print("tested",a,b,"%3.3f"%(time()-tt2))
            totest.remove(a)
            print(totest)

    res=set()
    for a in data:
        for b in a["scanner"]:
            res.add( str(b[0]+a["diff"][0])+","+str(b[1]+a["diff"][1])+","+str(b[1]+a["diff"][1]) )
    print("result",len(res))

    with open("diffs.txt","w") as f:
        for a in data:
            print(a["diff"][0],a["diff"][1],a["diff"][2],file=f)


#-----------------------------

def scanner_overlap(a,b):

    matchcount=12
    if "orients" not in b:
        b["orients"]=generate_scanner_orientations(b["scanner"])
    s=a["scanner"]

    hit=0
    seen=set()
    for t in b["orients"]:
        for xs in s:
            for xt in t:
                d0=xs[0]-xt[0]; d1=xs[1]-xt[1]; d2=xs[2]-xt[2]
                v=d0+(d1*10000)+(d2*100000000)
                # if v in seen: continue
                seen.add(v)
                hit=0
                j1=len(t)
                for ys in range(len(s)):
                    j2=len(s)
                    for yt in range(len(t)):
                            # print(s[ys],t[yt],d0,d1,d2)
                        if s[ys][0]==t[yt][0]+d0 and s[ys][1]==t[yt][1]+d1 and s[ys][2]==t[yt][2]+d2:
                            hit+=1
                            # if d0==68 and d1==-1246 and d2==-43:
                            #     print(hit)
                            if hit>=matchcount:
                                b["scanner"]=t
                                b["found"]=True
                                b["diff"]=[a["diff"][0]+d0,a["diff"][1]+d1,a["diff"][2]+d2]
                                return True
                        j2-=1
                        # if j2+hit<matchcount: break
                    j1-=1
                    # if j1+hit<matchcount: break


    return False    

def generate_scanner_orientations(scanner):

    result=[]
    for x in range(24): result.append([])
    for becon in scanner:
        for i,p in enumerate(xyz(becon)):
            result[i].append(p)
    return result

def xyz(p):
    x=p[0] ; y=p[1] ; z=p[2]
    result=[]
    for f in [[x,y,z],[x,z,-y],[x,-y,-z],[x,-z,y],[z,y,-x],[-z,y,x]]:
        result.append( [ f[0], f[1], f[2]] )
        result.append( [-f[1], f[0], f[2]] )
        result.append( [-f[0],-f[1], f[2]] )
        result.append( [ f[1],-f[0], f[2]] )
    return result

separator()
main()
separator()
