#!/usr/bin/python3

import re
from shared import style_list,in_file,grep,header,footer,printtable

def main():
    
    data=in_file("rawdata")

    total=""
    for line in data:
        if total=="":
            total=line
        else:
            total=sfadd(total,line)
    
    print("PART 1")
    print("total =",total)
    print("magnitude =",sfmagnitude(total))

    footer()

    print("PART 2")
    results=[]
    for a in range(0,len(data)):
        print(".",end="",flush=True)
        for b in range(a+1,len(data)):
            results.append( int( sfmagnitude( sfadd(data[a],data[b]) ) ) )
            results.append( int( sfmagnitude( sfadd(data[b],data[a]) ) ) )
    print("")
    print("largest magnitude =",max(results))



#-----------------------------

def sfadd(a,b):
    # add 2 sf numbers together
    # and then reduce result
    num="["+a+","+b+"]"
    while True:
        exploderes=sfexplode(num)
        if num!=exploderes:
            num=exploderes
        else:
            splitres=sfsplit(num)
            if num!=splitres:
                num=splitres
            else:
                break    
    return(num)

def sfexplode(sfnum):

    cnt=0
    level=0
    while cnt<len(sfnum):
        if sfnum[cnt]=="[": level+=1
        if sfnum[cnt]=="]": level-=1
        if level>4:
            
            # match a number pair in square breackets
            m=list_matches("\[\d+,\d+\]",sfnum[cnt:])
            if len(m)==0: return sfnum
            before=sfnum[0:cnt+m[0]["start"]]
            matched=m[0]["str"]
            after=sfnum[cnt+m[0]["end"]:]
            
            # grab integers (x and y) out of matched pattern
            m=list_matches("\d+",matched)
            x=int(m[0]["str"])
            y=int(m[1]["str"])

            # add x to right most number in 'before'
            m=list_matches("\d+",before)
            if len(m)>0:
                x=str(int(m[-1]["str"])+x)
                before=before[0:m[-1]["start"]]+x+before[m[-1]["end"]:]
                
            # add y to right most number in 'after'            
            m=list_matches("\d+",after)
            if len(m)>0:
                y=str(int(m[0]["str"])+y)
                after=after[0:m[0]["start"]]+y+after[m[0]["end"]:]
            
            # return recalcuulated sfnum
            return before+"0"+after
        cnt+=1
    return sfnum
        
def sfsplit(sfnum):
    # split the first number > 9 into bracketed pair
    # that will be the first 2 digit number in the sfnum string
    m=list_matches("[0-9][0-9]+",sfnum)
    if len(m)>0 :
        a=int(int(m[0]["str"])/2)
        b=int((int(m[0]["str"])/2)+0.5)
        ab="["+str(a)+","+str(b)+"]"
        sfnum = sfnum[0:m[0]["start"]] + ab + sfnum[m[0]["end"]:]

    return(sfnum)

def list_matches(m,s):
    # returns a list of dicts
    # a list of the start, end, and matching str 
    res=[]
    for match in re.finditer(m,s):
        res.append( {"start":match.start(), "end":match.end(), "str":s[match.start():match.end()] } )
    return res

def sfmagnitude(sfnum):

    # loop through sfnum repeatigly simplifying
    # until just a single number left
    while True:
        # find bracketed pair
        m=list_matches("\[\d+,\d+\]",sfnum)
        if len(m)==0: return sfnum
        before=sfnum[0:m[0]["start"]]
        matched=m[0]["str"]
        after=sfnum[m[0]["end"]:]
        
        # grab integers (x and y) out of matched pattern
        m=list_matches("\d+",matched)
        mag=(3*int(m[0]["str"]))+(2*int(m[1]["str"]))
        sfnum=before+str(mag)+after

def strdiff(a,b):
    
    # used for debugging - highlights what has chanegd in the middle of a string
    c=0
    res=["","",""]
    while True:
        if a[c]!=b[c]: break
        res[0]+=a[c]
        c+=1
    c=1
    while True:
        if a[-c]!=b[-c]: break
        res[2]=a[-c]+res[2]
        c+=1
    res[1]=b[len(res[0]):0-len(res[2])]    
    return ("__".join(res))
            
    
header()
main()
footer()
