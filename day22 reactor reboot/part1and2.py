#!/usr/bin/python3 -u

import re
import sys
from pprint import pprint
from shared import style_list,in_file,grep,separator,printtable
from time import time

inputfile="rawdata"

def main(regions):

    lasta=0
    while True:
        # get next pair to compare
        (a,b)=next_to_process(regions,lasta)
        lasta=a

        # when no more cuboid to split break out of loop
        if a<0: break 

        # break up overlapping cubes into smaller cubes
        addr=breakup_region(regions[a],regions[b])
        regions=regions[0:a]+addr+regions[a+1:]
        
    # now that all cuboids are no longer overlapping 
    # we cound the volume of each cube that is "on" to get final result
    onlights=0
    for n in regions:
        if n[0]=="off": continue
        onlights+= ((n[2]-n[1])+1) * ((n[4]-n[3])+1) * ((n[6]-n[5])+1)
    return onlights

#==============================

def next_to_process(r,x):

    # look next overlapping cube
    for a in range(x,(len(r)-1)):
        for b in range(a+1,len(r)):
            j = calculate_overlap(r[a],r[b])
            if len(j)!=0: return (a,b) # return if overlap found

    # no overlap found
    return (-1,-1)
            
def calculate_overlap(a,b):

    # reject when no overlap
    if a[1]>b[2] or a[2]<b[1] or a[3]>b[4] or a[4]<b[3] or a[5]>b[6] or a[6]<b[5]:
        return []

    # calculate inner overlap
    x=[a[1],a[2],b[1],b[2]] ; x.sort()
    y=[a[3],a[4],b[3],b[4]] ; y.sort()
    z=[a[5],a[6],b[5],b[6]] ; z.sort()
    result=[b[0],x[1],x[2],y[1],y[2],z[1],z[2]]
    
    return result


def breakup_region(a,b):

    i=99999999 # infinity
    s=a[0] # status to set

    # each cube is split into 26 subcubes (3x3x3 - central cube)
    co=calculate_overlap(a,b)
    overlaps=[]
    x1=co[1] ; x2=co[2]; y1=co[3]; y2=co[4]; z1=co[5]; z2=co[6]

    overlaps.append( calculate_overlap( a,   [s, -i,x1-1 , -i,y1-1 , -i,z1-1  ] ) )
    overlaps.append( calculate_overlap( a,   [s, -i,x1-1 , y1,y2   , -i,z1-1 ] ) )
    overlaps.append( calculate_overlap( a,   [s, -i,x1-1 , y2+1,i  , -i,z1-1 ] ) )
    overlaps.append( calculate_overlap( a,   [s, x1,x2   , -i,y1-1 , -i,z1-1 ] ) )
    overlaps.append( calculate_overlap( a,   [s, x1,x2   , y1,y2   , -i,z1-1 ] ) ) 
    overlaps.append( calculate_overlap( a,   [s, x1,x2   , y2+1,i  , -i,z1-1 ] ) )
    overlaps.append( calculate_overlap( a,   [s, x2+1,i  , -i,y1-1 , -i,z1-1 ] ) )
    overlaps.append( calculate_overlap( a,   [s, x2+1,i  , y1,y2   , -i,z1-1 ] ) )
    overlaps.append( calculate_overlap( a,   [s, x2+1,i  , y2+1,i  , -i,z1-1 ] ) )

    overlaps.append( calculate_overlap( a,   [s, -i,x1-1 , -i,y1-1 , z1,z2   ] ) )
    overlaps.append( calculate_overlap( a,   [s, -i,x1-1 , y1,y2   , z1,z2   ] ) )
    overlaps.append( calculate_overlap( a,   [s, -i,x1-1 , y2+1,i  , z1,z2   ] ) )
    overlaps.append( calculate_overlap( a,   [s, x1,x2   , -i,y1-1 , z1,z2   ] ) )
    # overlaps.append( b )  # centre
    overlaps.append( calculate_overlap( a,   [s, x1,x2   , y2+1,i  , z1,z2   ] ) )
    overlaps.append( calculate_overlap( a,   [s, x2+1,i  , -i,y1-1 , z1,z2   ] ) )
    overlaps.append( calculate_overlap( a,   [s, x2+1,i  , y1,y2   , z1,z2   ] ) )
    overlaps.append( calculate_overlap( a,   [s, x2+1,i  , y2+1,i  , z1,z2   ] ) )

    overlaps.append( calculate_overlap( a,   [s, -i,x1-1 , -i,y1-1 , z2+1,i  ] ) )
    overlaps.append( calculate_overlap( a,   [s, -i,x1-1 , y1,y2   , z2+1,i  ] ) )
    overlaps.append( calculate_overlap( a,   [s, -i,x1-1 , y2+1,i  , z2+1,i  ] ) )
    overlaps.append( calculate_overlap( a,   [s, x1,x2   , -i,y1-1 , z2+1,i  ] ) )
    overlaps.append( calculate_overlap( a,   [s, x1,x2   , y1,y2   , z2+1,i  ] ) )  
    overlaps.append( calculate_overlap( a,   [s, x1,x2   , y2+1,i  , z2+1,i  ] ) )
    overlaps.append( calculate_overlap( a,   [s, x2+1,i  , -i,y1-1 , z2+1,i  ] ) )
    overlaps.append( calculate_overlap( a,   [s, x2+1,i  , y1,y2   , z2+1,i  ] ) )
    overlaps.append( calculate_overlap( a,   [s, x2+1,i  , y2+1,i  , z2+1,i  ] ) )

    # strip out empty subcubes and return resulting new cubes 
    result=[]
    for n in overlaps:
        if len(n)>0 :
            result.append(n) 
    return result


def get_data(inputfile,coreonly=True):

    # loads data in
    # coreonly used to define if to take into account outside of +/-50 x/y/z
    raw=in_file(inputfile)
    data=[]
    for line in raw:
        data.append( re.split("[^-0-9onf]+",line) )
        for n in range(1,len(data[-1])):
            data[-1][n]=int(data[-1][n])
        if coreonly and abs(data[-1][1])>50:
            data.pop()

    return data

#==============================

separator()
print("part1",main(get_data(inputfile)))
print("part2",main(get_data(inputfile,coreonly=False)))
separator()
