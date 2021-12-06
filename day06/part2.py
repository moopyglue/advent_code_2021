
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
    fish[0]=fish[1]
    fish[1]=fish[2]
    fish[2]=fish[3]
    fish[3]=fish[4]
    fish[4]=fish[5]
    fish[5]=fish[6]
    fish[6]=fish[7]+birthing_fish
    fish[7]=fish[8]
    fish[8]=birthing_fish

    print(n+1,fish)

# sum array elements for result
print("result =",sum(fish))

print("¬"*100)
