
import common

file="rawdata"
bingocalls = common.load_bingo_calls(file)
cards      = common.load_cards(file)

# for each bingo call ...
for a in range(len(bingocalls)):
    called=bingocalls[0:a+1]
    removed=0
    # for each card ...
    for b in range(len(cards)):
        # delete cards as they match - tracking the last one removed(last_card)
        # we need to track the number 'removed' during this loop because the
        # size of the list changes as we delete more cards
        if common.check_card(cards[b-removed],called):
            last_card=cards[b-removed].copy()
            del cards[b-removed]
            removed+=1
    if len(cards)==0: break

# results printing
sm=common.sum_unmarked(last_card,called)
print("last_card",last_card)
print("sum_unmarked=%d, lastcalled=%s" % (sm,called[-1] ))
print("result=%d" % (sm*int(called[-1])))
      