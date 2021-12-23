#!/usr/bin/python3

import re
import sys
from pprint import pprint
from shared import style_list,in_file,grep,separator,printtable
from time import time

inputfile="sample"

ddice_last=0
ddice_rolls=0

def main(inputfile):

    data=style_list("numlist",in_file(inputfile))
    players=[[10,0],[3,0]]
    
    pprint(players)
    while True:
        for player in range(len(players)):
            players[player][0]+=(ddice()+ddice()+ddice())%10
            if players[player][0] > 10 :
                players[player][0]-=10
            players[player][1]+=players[player][0]
            pprint(players)
            if players[player][1]>=1000:
                print("rolls",ddice_rolls)
                exit(0)

#==============================

def ddice():
    global ddice_last,ddice_rolls
    ddice_last+=1
    if ddice_last>1000: ddice_last=1
    ddice_rolls+=1
    return ddice_last

#==============================

separator()
main(inputfile)
separator()
