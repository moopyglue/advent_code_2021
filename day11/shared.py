
import re

# general file input routine to make importing data quicker
# at beinging of each day (maybe :¬)
def infile(filename,style="normal",start=1,end=999999):
    
    result=[]
    with open(filename) as inputfile:
        line=0
        for n in inputfile.readlines():
            
            n=n.strip()
            
            # filter lines based on start,end
            line+=1
            if line<start or line>end:
                continue
            
            # everything except digits is a seperator
            if style=="numarray":
                l=[]
                for num in re.split("[^0-9]+",n):
                    l.append(int(num))
                result.append(l)
            
            # everything except alphanumerica is a seperator
            elif style=="alphanumarray":
                l=[]
                for word in re.split("[^0-9a-zA-Z]+",n):
                    l.append(word)
                result.append(l)
            
            # compressed digit array
            elif style=="digitarray":
                l=[]
                for c in range(len(n)):
                    l.append(int(n[c]))
                result.append(l)
            
            # just read line in as is
            else:
                result.append(n)
        
        # where aray or arrays is for only 1 array then make
        # single dimentional array
        if len(result)==1:
            result=result[0]
            
    return result
