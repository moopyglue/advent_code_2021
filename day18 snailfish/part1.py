#!python.exe

import re
from shared import style_list,in_file,grep,header,footer,printtable

def main():
    
    data=in_file("sampley")
    print(data)
    total=""
    for line in data:
        if total=="":
            total=line
        else:
            total=sfadd(total,line)
    
    print("\ntotal =",total)
    exit(0)
    
#-----------------------------

def sfadd(a,b):
    num="["+a+","+b+"]"
    print("\nnew      ",num)
    while True:
        exploderes=sfexplode(num)
        if num!=exploderes:
            print("explode",strdiff(num,exploderes))
            num=exploderes
        else:
            splitres=sfsplit(num)
            if num!=splitres:
                print("split  ",strdiff(num,splitres))
                num=splitres
            else:
                break    
    print("sfadd()  ",num)
    return(num)

def sfexplode(n):
    stack=[]
    level=0
    action=False
    next_int_addition=0
    while len(n)>0:
        
        m=re.search("^\[|\]|,|[0-9]+|_",n).group(0)
        #print(m," | ",stack)

        if m=="[":
            level+=1
            stack.append(m)
            
        elif m=="]":
            right=stack.pop()
            left=stack.pop()
            discard=stack.pop() # discard bracket
            if level>4 and not action:
                mm=0
                stack=stack_left_num_add(stack,left)
                next_int_addition=right
                #print("exploded ",stack,left,right)
                action=True
            else:
                mm="["+str(left)+","+str(right)+"]"
            stack.append(mm)
            level-=1
            
        elif m!=",": # we found a integer
            stack.append(int(m)+next_int_addition)
            next_int_addition=0
            
        n=n[len(m):]
    return stack[0]
    
def sfsplit(n):
    m=re.search("[0-9][0-9]+",n)
    if m :
        a=int(int(m.group(0))/2)
        b=int((int(m.group(0))/2)+0.5)
        n=n[0:m.span()[0]] + "["+str(a)+","+str(b)+"]"+n[m.span()[1]:]

    return(n)

def stack_left_num_add(stack,num):
    for r in range(len(stack)-1,1,-1):
        #print("stack_left_num_add()")
        if isinstance(stack[r],int):
            stack[r]+=num
            #print(stack)
            return stack
        if isinstance(stack[r],str):
            p = re.compile("[0-9]+")
            # print("findstr")
            nn=stack[r]
            for x in p.finditer(stack[r]):
                st=x.start()
                en=x.end()
                nn=stack[r][0:st]+str(int(stack[r][st:en])+num)+stack[r][en:]
            if nn!=stack[r]:
                stack[r]=nn
                #print(stack)
                return stack
    return stack
                
def strdiff(a,b):
    
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
    return ("___".join(res))
            
    
header()
main()
footer()
