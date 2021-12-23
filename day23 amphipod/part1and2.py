#!/usr/bin/python3

import re
import sys
from pprint import pprint
from shared import style_list,in_file,grep,separator,printtable
from time import time

inputfile="sample2"

map=set()

def main(data):

    pprint(data)
    
#==============================

def get_data(inputfile):

    raw=in_file(inputfile)

    return raw

#==============================

separator()
main(in_file(inputfile))
separator()
