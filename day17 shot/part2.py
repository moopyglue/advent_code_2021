
from shared import style_list,in_file,grep,header,footer

def main():
    
    targetbox=style_list("numlist",in_file("rawdata"))
    print("targetbox",targetbox)
    tleft=targetbox[0][0] # target x minimum 
    tright=targetbox[0][1] # target x maximum  
    ttop=targetbox[0][3] # target y maximum
    tbottom=targetbox[0][2] # target y minimum 

    # choose x and y velocity ranges
    xstart=0 ; xstop=tright
    ystop=tbottom; ystart=(tbottom-1)*-1 
    growing=0
    while growing<tleft:
        xstart+=1 ; growing+=xstart
    print("velocities: xrange:",xstart,xstop,"yrange:",ystart,ystop)
    
    results=set()
    # start_vx = starting velocity of x
    for start_vx in range(xstart,xstop+1,1):
        
        # start_vy = starting velocity of y
        for start_vy in range(ystart,ystop-1,-1): 
            
            x=0 ; y=0      # start at the origin
            vx=start_vx    # changeing velocity of x stored in xv
            vy=start_vy    # changeing velocity of y stored in xy
            
            # loop through each step stopping when overshoot target 
            while True:
                x+=vx ; y+=vy
                if vx>0 : vx-=1
                vy-=1
                if x>tright or y<tbottom:
                    break
                if x>=tleft and y<=ttop :
                    results.add( (start_vx,start_vy) )
                    break
    
    # restaults stored in set() to ignore duplicates
    print("velocities successful",len(results))

#-----------------------------

header()
main()
footer()
