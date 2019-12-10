import BJ_utils as bj
# Need to have an output for when the shoe runs out of cards before the hand is finished
def play_dealer_strategy(shoe,hand,h17):
    if h17:
        while len(bj.hand_count(hand)) !=0 and max(bj.hand_count(hand)) <=17:
            if len(bj.hand_count(hand)) ==1 and max(bj.hand_count(hand)) ==17:
                return hand
            else:
                hand = bj.hit(shoe,hand)
        return hand
    else:
        while len(bj.hand_count(hand)) !=0 and max(bj.hand_count(hand)) < 17:
            hand = bj.hit(shoe,hand)
        return hand

# print('complete')