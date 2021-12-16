
from shared import style_list,in_file,grep,header,footer
import re

header()
#-----------------------------

hexmap={"0":"0000","1":"0001","2":"0010","3":"0011","4":"0100",
        "5":"0101","6":"0110","7":"0111","8":"1000","9":"1001",
        "A":"1010","B":"1011","C":"1100","D":"1101","E":"1110",
        "F":"1111"}

level=0
def parse(b):
    
    global level,vertot
    level+=1
    lstr=">"*(level-1)

    version=int(b[0:3],2)
    vertot+=version
    type=int(b[3:6],2)
    b=b[6:]
    #print("\n"+lstr,"ver",version,"vertot",vertot,"typ",type,end=" ")
    
    if type==4:
        n=""
        while True:
            n+=b[1:5]
            if b[0]=="0": break
            b=b[5:]
        b=b[5:]
        #print("literal",int(n,2),"remain_length",len(b),end="")
        result=int(n,2)
    else:
        res=[]
        if b[0]=="0":
            length=int(b[1:16],2)
            b=b[16:]
            #print("operator0 length",length,"packet",end="")
            subpack=b[:length]
            b=b[len(subpack):]
            while len(subpack)>8:
                (subpack,subresult)=parse(subpack)
                res.append(subresult)
                
        else: # b[0]="1"
            count=int(b[1:12],2)
            b=b[12:]
            #print("operator1 count",count,end="")
            while count>0:
                (b,subresult)=parse(b)
                res.append(subresult)
                count-=1
        
        result=0
        if type <=3 : 
            result=res[0]
            for n in res[1:]:
                if type==0: result+=n
                if type==1: result*=n
                if type==2 and n<result: result=n
                if type==3 and n>result: result=n   
        else: 
            if type==5 and res[0]>res[1]: result=1
            if type==6 and res[0]<res[1]: result=1
            if type==7 and res[0]==res[1]: result=1
                            
    
    #print("\n"+lstr,"result",result,end="")
    level-=1
    return [b,result]

data=style_list("normal",in_file("rawdata"))

vertot=0
bitdata=""

for n in data[0]:
    bitdata+=hexmap[n]

(b,result)=parse(bitdata)
print("part1","vertot",vertot)
print("part2","result",result)

#-----------------------------
footer()
