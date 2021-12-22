#!/usr/bin/python3

import re
import sys
from pprint import pprint
from shared import style_list,in_file,grep,separator,printtable
from time import time

inputfile="rawdata"
loopcount=50

decoder=""
map=""

def main(inputfile):

    global decoder,map,loopcount

    decoder=tobinary(in_file(inputfile, end=1)[0])     # read in decoder string
    map=in_file(inputfile, start=3)  # read in floor map
    for a in range(len(map)):
        map[a]=tobinary(map[a])

    for n in range(loopcount):
        ttype="0"
        if int(n/2)!=(n/2):
            ttype=decoder[0]
        map=remap(map,decoder,ttype)
        print("after",n+1,"interation we have",countstr("".join(map)),"lit")

# --------

def tobinary(s):
    res=""
    for a in s:
        if a=="#": res+="1"
        else: res+="0"
    return res

def pad(sa,c):
    newsa=[ c*(len(sa[0])+2) ] 
    for n in sa:
        newsa.append(c+n+c)
    newsa.append(c*(len(sa[0])+2))
    return newsa

def remap(map,decoder,padding):

    map=map.copy()
    newmap=[]
    map=pad(map,padding)
    map=pad(map,padding)
    for y in range(len(map)-2):
        newmap.append("")
        for x in range(len(map[y])-2):
            k=map[y][x:x+3]+map[y+1][x:x+3]+map[y+2][x:x+3]
            newmap[-1]+=decoder[int(k,2)]
    return newmap

def countstr(s):
    c=0
    for n in range(len(s)):
        if s[n]=="1": c+=1
    return c

#==============================

separator()
main(inputfile)
separator()
