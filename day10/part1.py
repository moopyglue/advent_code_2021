
import shared

print("¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬")

data=shared.infile("rawdata",style="normal")

score=0
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
        # where an error occurs increase score as per problem
        else:
            if line[n] == ')': score+=3
            if line[n] == ']': score+=57
            if line[n] == '}': score+=1197
            if line[n] == '>': score+=25137
            print(stack)
            break

#result
print("result =",score)
       
print("¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬")
