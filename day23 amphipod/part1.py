#!/usr/bin/python3

from os import O_NOFOLLOW, ttyname
import re
import sys
from pprint import pprint
from shared import style_list,in_file,grep,separator,printtable
from time import time


def main():

    template=[ "+-----------+",
               "|XX.X.X.X.XX|",
               "+-+A:B:C:D+-+",
               "  |A:B:C:D|  ",
               "  +-------+  " ]
    
    locations=set()
    lookup={"X":0, "A":0, "B":0, "C":0, "D":0, ".":0 }
    namelocs={}

    for a in range(len(template)):
        for b in range(len(template[a])):
            if template[a][b] in "ABCDX.":
                lookup[template[a][b]]+=1
                namelocs[template[a][b]+str(lookup[template[a][b]])]=[template[a][b],a,b]
                locations.add( (a,b ))
                template[a]=("%s.%s"%(template[a][0:b],template[a][b+1:]))
    #print(namelocs)

    
    paths={}
    paths.update(make_routes("ABCD","X",namelocs))
    paths.update(make_routes("X","ABCD",namelocs))
    for k in [ l for l in paths if l[1][1]=="2" and l[1][0] <= 'D' ]:
        paths.pop(k)
    paths[('A1','A2')]=[[2,3],[3,3]]
    paths[('B1','B2')]=[[2,5],[3,5]]
    paths[('C1','C2')]=[[2,7],[3,7]]
    paths[('D1','D2')]=[[2,9],[3,9]]

    # for k in paths:
    #     print(k,paths[k])
    traveling=style_list("alphanumlist",in_file("sample"))
    for t in traveling:
        t.append([])
        t.append(0)

    pprint(traveling)

    follow_paths(traveling,paths)

    exit(0)
    
#==============================

ooo=0

def follow_paths(travellers,paths):

    global ooo
    ooo+=1
                
    aps=avail_paths(travellers,paths)
    # pprint(aps)

    if ooo>66:
        return

    for ap in range(len(aps)):
        for t in range(len(travellers)):
            if aps[ap][1]==travellers[t][1]:
                already_visited=False
                for p in travellers[t][3]:
                    if p==aps[ap][2]:
                        already_visited=True
                        break
                if not already_visited:
                    j=travellers.copy()
                    j[t][3].append(j[t][1])
                    j[t][1]=aps[ap][2]
                    j[t][4]+=aps[ap][3]
                    follow_paths(j,paths)
                break

    ooo-=1
    pprint(travellers)
    return


def avail_paths(travellers,paths):

    endpaths=[]

    occupied=set()
    for t in travellers:
        for p in paths:
            if t[1]==p[0]:
                occupied.add( (paths[p][0][0],paths[p][0][1]))

    for t in travellers:
        loc=t[1]
        for p in paths:
            if p[0]!=loc: continue                       # skip routes not starting at my location
            if p[0][0]=="X" and p[1][0]!=t[0]: continue  # 'A's must end up in 'A'
            # weed out paths with obsructions
            cnt=0
            for k in paths[p]:
                if (k[0],k[1]) in occupied:
                    cnt+=1
            if cnt>1:
                continue
            # weed out paths which have completed
            endpaths.append( [ t[0], p[0], p[1], (int(len(paths[p])-1)*int(t[2])) ] )
    
    # remove any [ABCD]1 routes when [ABCD]2 routes are available
    for k in ["A","B","C","D"]:
        j1=-1 ; j2=-1
        for l in range(len(endpaths)):
            if endpaths[l][2]==k+"1": j=l
            if endpaths[l][2]==k+"2": j=l
        if j2>=0:
            endpaths=endpaths[0:j1]+endpaths[j1+1:]
            
    return endpaths
        
def make_routes(start,finish,names):

    def single_route(a,b):
        r=[a]
        while a[0]>b[0]:
            a=[a[0]-1,a[1]]
            r.append(a)
        while a[1]>b[1]:
            a=[a[0],a[1]-1]
            r.append(a)
        while a[1]<b[1]:
            a=[a[0],a[1]+1]
            r.append(a)
        while a[0]<b[0]:
            a=[a[0]+1,a[1]]
            r.append(a)
        return r

    result={}
    locs=set()
    for a in names:
        locs.add((names[a][1],names[a][2]))

    for s in start:
        for f in finish:
            for ns in names:
                if names[ns][0]!=s: continue
                for nf in names:
                    if names[nf][0]!=f: continue
                    result[(ns,nf)]=single_route(names[ns][1:],names[nf][1:]) 
    return result

#==============================

separator()
main()
separator()
