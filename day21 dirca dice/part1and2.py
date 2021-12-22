#!/usr/bin/python3

import re
import sys
from pprint import pprint
from shared import style_list,in_file,grep,separator,printtable
from time import time

inputfile="sample"

def main(inputfile):

    data=style_list("numlist",in_file(inputfile))     
    print(data)

#==============================


#==============================

separator()
main(inputfile)
separator()
