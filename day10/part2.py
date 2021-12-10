
import shared

print("¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬")

data=shared.infile("rawdata",style="normal")

totalscore=[]
for line in data:
    
    stack=[]
    for n in range(len(line)):

        # add opening brackets to the stack
        if line[n] in ['<','{','(','[']:
            stack.append(line[n])

        # remove correctly matched closing brackets from the stack
        elif ( 
              ( stack[-1] == '<' and line[n] == '>' ) or 
              ( stack[-1] == '{' and line[n] == '}' ) or 
              ( stack[-1] == '(' and line[n] == ')' ) or 
              ( stack[-1] == '[' and line[n] == ']' )
        ):
            stack.pop()

        # if an error clear the stack (so no score) and break out
        else:
            stack=[]
            break
    
    # skip errors and fully correct lines
    if len(stack) == 0 : continue

    # calculate  scheme and discard error values
    linescore=0
    for n in range(len(stack)):
        linescore*=5
        if stack[-1] == '<': linescore+=4
        if stack[-1] == '{': linescore+=3
        if stack[-1] == '(': linescore+=1
        if stack[-1] == '[': linescore+=2
        stack.pop()
    totalscore.append(linescore)

# result
totalscore.sort()
print(totalscore)
print("result =",totalscore[int((len(totalscore)-1)/2)])
       
print("¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬")
