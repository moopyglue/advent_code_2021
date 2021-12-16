
from shared import style_list,in_file,grep,header,footer

def main():
    data=style_list("digitlist",in_file("rawdata"))
    print("part1",lowest_risk(data,len(data)))
    print("part2",lowest_risk(data,len(data)*5))

def lowest_risk(data,square):
    
    risk_so_far={ (0,0):0 }
    visited=set()
    to_visit=set() ; to_visit.add( (0,0) )
    
    while len(to_visit)>0:

        # find node in to_visit with lowest risk and visit it  
        node=sorted(to_visit, key=lambda k: risk_so_far[k])[0]
        to_visit.remove(node)
        visited.add(node)
        
        # loop through options to move right,left,down,up
        possible_moves=[ (node[0],node[1]+1), (node[0]+1,node[1]),
                         (node[0],node[1]-1), (node[0]-1,node[1]) ]
        for next in possible_moves:
            
            if next in visited : continue # ignore already visited
            if next[0]<0 or next[1]<0 or next[0]>=square or next[1]>=square:
                continue # ignore out of bounds

            newrisk=get_value(data,next)+risk_so_far[node]
            if ( next not in risk_so_far ) or  ( risk_so_far[next]> newrisk ):
                # if node not seen before or proposed risk smaller...
                risk_so_far[next]=newrisk
                to_visit.add(next)
    
    # return the lowest risk value for the designated exit point
    return risk_so_far[ (square-1,square-1) ]

def get_value(data,n):
    # if point is out of bounds of data then caclculate modulus value
    # as per problem statement. (saves creating 25x data array)
    width=len(data)
    v=data[n[0]%width][n[1]%width]
    add=int(n[0]/width)+int(n[1]/width)
    return (((v+add)-1)%9)+1

#-----------------------------

header()
main()
footer()
