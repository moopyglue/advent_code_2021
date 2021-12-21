#!/usr/bin/python3

# Played around wit this making it faster
# on slow core i3 took 11 mins 
# believ it can be reduced in time by at least half

import re
import sys
from pprint import pprint
from shared import style_list,in_file,grep,separator,printtable
from time import time

def main():
    
    tt=time()

    # load in data[]
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
    
    # loop through matches 
    # each loop totest() is added to and removed until empty
    totest=set()
    totest.add(0)
    data[0]["found"]=data[0]["scanner"]
    while len(totest)>0:
        for a in list(totest):
            for b in range(len(data)):
                if "found" in data[b]: continue
                if scanner_overlap(data[a],data[b]):
                    print("found",b,data[b]["diff"])
                    totest.add(b)
            totest.remove(a)
    print("time taken %3.1fs"%(time()-tt))

    # create results set() to remove duplicate becons
    # to get unique becons count (part1 result) 
    res=set()
    for a in data:
        for b in a["scanner"]:
            res.add( str(b[0]+a["diff"][0])+","+str(b[1]+a["diff"][1])+","+str(b[1]+a["diff"][1]) )
    print("part1",len(res))

    # calculate manhatten distances and keep max (part2 result) 
    max=0
    for a in range(len(data)):
        for b in range(len(data)):
            c=abs(data[a]["diff"][0]-data[b]["diff"][0])
            c+=abs(data[a]["diff"][1]-data[b]["diff"][1])
            c+=abs(data[a]["diff"][2]-data[b]["diff"][2])
            if c>max:
                max=c
    print("part2",max)

#-----------------------------

def scanner_overlap(a,b):

    # looks for an overlap
    # if it find 1 it
    # - returns True
    # - sets the "scanner" value to the correctly oriention
    # - sets "found" to True
    # - creates the triple diff[] tuple showing relative
    #   location to origin scanner
    if "orients" not in b:
        b["orients"]=generate_scanner_orientations(b["scanner"])
    s=a["scanner"]

    def check(d0,d1,d2,s,t):
        hit=0
        matchcount=12
        for ys in range(len(s)):
            for yt in range(len(t)):
                if s[ys][0]!=t[yt][0]+d0: continue
                if s[ys][1]!=t[yt][1]+d1: continue
                if s[ys][2]!=t[yt][2]+d2: continue
                hit+=1
                if hit>=matchcount:
                    return True

    seen=set()
    for t in b["orients"]:
        for xs in s:
            for xt in t:
                d0=xs[0]-xt[0]; d1=xs[1]-xt[1]; d2=xs[2]-xt[2]
                if check(d0,d1,d2,s,t):
                    b["scanner"]=t
                    b["found"]=True
                    b["diff"]=[a["diff"][0]+d0,a["diff"][1]+d1,a["diff"][2]+d2]
                    return True
    return False    

def generate_scanner_orientations(scanner):

    # generate all combinations of posisble orientations
    # for a single scanner.

    def xyz(p):
        x=p[0] ; y=p[1] ; z=p[2]
        result=[]
        for f in [[x,y,z],[x,z,-y],[x,-y,-z],[x,-z,y],[z,y,-x],[-z,y,x]]:
            result.append( [ f[0], f[1], f[2]] )
            result.append( [-f[1], f[0], f[2]] )
            result.append( [-f[0],-f[1], f[2]] )
            result.append( [ f[1],-f[0], f[2]] )
        return result

    result=[]
    for x in range(24): result.append([])
    for becon in scanner:
        for i,p in enumerate(xyz(becon)):
            result[i].append(p)
    return result


separator()
main()
separator()
