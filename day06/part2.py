
print("_"*100)

# define constants
birthcycle=7
new_birthcycle=9
cycle_days=256

# create an list of grouped values for number of fish
# e.g. if there are 2 fish that have 3 days before the
# spawn then fish[3]=2
fish=[0]*new_birthcycle
with open("rawdata") as inputfile:
    for n in inputfile.readline().strip().split(","):
        fish[int(n)]+=1

# update the list(fish) in a loop for 'cycledays'
# based on the described algorythm
for n in range(cycle_days):
    birthing_fish=fish[0]
    for c in range(new_birthcycle-1):
        fish[c]=fish[c+1]
    fish[birthcycle-1]+=birthing_fish
    fish[new_birthcycle-1]=birthing_fish
    print(n+1,fish)

# sum array elements for result
print("result =",sum(fish))

print("¬"*100)
