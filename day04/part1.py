
import common
import os

print(os.getcwd())

file="rawdata"
bingocalls = common.load_bingo_calls(file)
cards      = common.load_cards(file)

# for each bingo call ...
for a in range(len(bingocalls)):

    called=bingocalls[0:a+1]
    # for each card ...
    for b in range(len(cards)):

        # check each card against numbers called so far
        if common.check_card(cards[b],called):
            # found first matching card and brealk from look
            first_card=cards[b].copy()
            break

    if 'first_card' in locals(): break

# results printing
sm=common.sum_unmarked(first_card,called)
print("first_card",first_card)
print("card=%d, sum_unmarked=%d, lastcalled=%s" % (b,sm,bingocalls[a] ))
print("result=%d" % (sm*int(bingocalls[a])))
