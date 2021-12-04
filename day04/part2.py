
def check_line (l,n):
    # check a line(l) of number s to see if they are all list of numbers called(n)
    for a in range(len(l)):
        if l[a] not in n: return False
    return True
        
def check_card (c,n):
    # card(c) and numbers called(n)
    # return if any horizontal line or card(c) is all in numbers called(n)
    for a in range(0,24,5):
        if check_line( c[a:a+5],n): return True
    # return if any vertical line or card(c) is all in numbers called(n)
    for a in range(5):
        if check_line( [c[a],c[a+5],c[a+10],c[a+15],c[a+20]], n): return True
    # no lines macthed
    return False

def sum_unmarked (c,n):
    # sum all the card(c) numbers which have not been called(n)
    sum=0
    for a in range(len(c)):
        if c[a] not in n: sum+=int(c[a])
    return sum

# read in the data file
with open('rawdata') as inputfile:
    data=inputfile.readlines()

# allocate data read in from file
# into list of bingocalls and an array of arrays for cards 
bingocalls = data[0].strip().split(",") 
cards=[]
for x in range(1,len(data),6):
    # join then split each 6 lines to make cards each as a single array of 25 values
    cards.append(" ".join(data[x:x+6]).split() )

# for each bingo call ...
for a in range(len(bingocalls)):
    removed=0
    # for each card ...
    for b in range(len(cards)):
        # delete cards as they match - tracking the last card removed
        # we need to track the number 'removed' during this loop because the
        # size of the list changes as we delete more cards
        if check_card(cards[b-removed],bingocalls[0:a+1]):
            last_card=cards[b-removed].copy()
            del cards[b-removed]
            removed+=1
    last_called=a
    if len(cards)==0: break

# found matching card caluclate reulst and print
print("last_card",last_card)
print("sum_unmarked=%d, lastcalled=%s" 
        % (sum_unmarked(last_card,bingocalls[0:last_called+1]),
           bingocalls[last_called] ))
print("result=%d" % 
        (sum_unmarked(last_card,bingocalls[0:last_called+1])*
         int(bingocalls[last_called])))
exit(0)
        
    
# print(cards)
# print(bingocalls)