import BJ_utils as bj
import dealer_utils as dlr
import player_utils as plr
import math



# returns a list of lists. Each list is an outcome of a player in the form [hand,dealer_hand,Any Busts?, You Won or Lost or Tied]
def play_round_with_strategy(shoe, h17):
    count = 0
    original_count = 0
    dealer_hand = []
    hand = []
    player_outcomes = []
    for i in range(2):
        hand.append(shoe.pop())
        dealer_hand.append(shoe.pop())
    # for card in hand:
    #     if card in [2, 3, 4, 5, 6]:
    #         count += 1
    #     elif card in ['A', 10]:
    #         count += (-1)
    #     else:
    #         count += 0
    # for card in dealer_hand:
    #     if card in [2, 3, 4, 5, 6]:
    #         count += 1
    #     elif card in ['A', 10]:
    #         count += (-1)
    #     else:
    #         count += 0

    dealer_value = bj.hand_count(dealer_hand)
    player_value = bj.hand_count(hand)
    if max(dealer_value) == 21:
            if max(player_value) == 21:
                player_outcomes.append([hand, dealer_hand, 'You and Dealer has Blackjack', 'push', 'sds'])
                return [player_outcomes, count]
            else:
                player_outcomes.append([hand, dealer_hand, 'Dealer has Blackjack', 'loss','sdds'])
                return [player_outcomes,count]
    elif max(bj.hand_count(hand)) == 21:
        player_outcomes.append([hand,dealer_hand,'Blackjack','win','sdsd'])
        return [player_outcomes,count]
    dealer_hand = dlr.play_dealer_strategy(shoe, dealer_hand, h17)
    hands = [hand]
    hands = plr.splitter(shoe,hands,dealer_hand[1])
    hands = plr.splitter(shoe,hands,dealer_hand[1])
    # print('player hand')
    # print(hands)
    # print('dealer hand')
    # print(dealer_hand)
    for hand in hands:
        hand_outcome = plr.play_strategy(shoe, [hand, 'continue'], dealer_hand,count)
        # hand_outcome = dlr.play_dealer_strategy(shoe, hand, h17)
        hand = hand_outcome[0]
        action = hand_outcome[1]
        dealer_value = bj.hand_count(dealer_hand)
        hand_value = bj.hand_count(hand)
        if len(hand_value) > 0:
            if len(dealer_value) == 0:
                player_outcomes.append([hand, dealer_hand, 'Dealer Busted', 'win',action])
            else:
                if max(dealer_value) < max(hand_value):
                    player_outcomes.append([hand, dealer_hand, 'Nothing Interesting happened', 'win',action])
                elif max(dealer_value) == max(hand_value):
                    player_outcomes.append([hand, dealer_hand, 'Nothing Interesting happened', 'push',action])
                else:
                    player_outcomes.append([hand, dealer_hand, 'Nothing Interesting happened', 'loss',action])
        else:
            player_outcomes.append([hand, dealer_hand, 'You Busted', 'loss',action])
        for hand in hands:
            for card in hand:
                if card in [2,3,4,5,6]:
                    original_count += 1
                elif card in ['A',10]:
                    original_count += (-1)
                else:
                    original_count += 0
        for card in dealer_hand:
            if card in [2, 3, 4, 5, 6]:
                original_count += 1
            elif card in ['A', 10]:
                original_count += (-1)
            else:
                original_count += 0

    return [player_outcomes,original_count]

# def play_round(shoe, h17,count):
#     # count = 0
#     dealer_hand = []
#     hand = []
#     player_outcomes = []
#     for i in range(2):
#         hand.append(shoe.pop())
#         dealer_hand.append(shoe.pop())
#     for card in hand:
#         if card in [2, 3, 4, 5, 6]:
#             count += 1
#         elif card in ['A', 10]:
#             count += (-1)
#         else:
#             count += 0
#     for card in dealer_hand:
#         if card in [2, 3, 4, 5, 6]:
#             count += 1
#         elif card in ['A', 10]:
#             count += (-1)
#         else:
#             count += 0
#
#     dealer_value = bj.hand_count(dealer_hand)
#     player_value = bj.hand_count(hand)
#     if max(dealer_value) == 21:
#             if max(player_value) == 21:
#                 player_outcomes.append([hand, dealer_hand, 'You and Dealer has Blackjack', 'push', 'sds'])
#                 return [player_outcomes, count]
#             else:
#                 player_outcomes.append([hand, dealer_hand, 'Dealer has Blackjack', 'loss','sdds'])
#                 return [player_outcomes,count]
#     elif max(bj.hand_count(hand)) == 21:
#         player_outcomes.append([hand,dealer_hand,'Blackjack','win','sdsd'])
#         return [player_outcomes,count]
#     dealer_hand = dlr.play_dealer_strategy(shoe, dealer_hand, h17)
#     hands = [hand]
#     hands = plr.splitter(shoe,hands,dealer_hand[1])
#     hands = plr.splitter(shoe,hands,dealer_hand[1])
#     for hand in hands:
#         hand_outcome = plr.play_strategy(shoe, [hand, 'continue'], dealer_hand)
#         # hand_outcome = dlr.play_dealer_strategy(shoe, hand, h17)
#         hand = hand_outcome[0]
#         action = hand_outcome[1]
#         dealer_value = bj.hand_count(dealer_hand)
#         hand_value = bj.hand_count(hand)
#         if len(hand_value) > 0:
#             if len(dealer_value) == 0:
#                 player_outcomes.append([hand, dealer_hand, 'Dealer Busted', 'win',action])
#             else:
#                 if max(dealer_value) < max(hand_value):
#                     player_outcomes.append([hand, dealer_hand, 'Nothing Interesting happened', 'win',action])
#                 elif max(dealer_value) == max(hand_value):
#                     player_outcomes.append([hand, dealer_hand, 'Nothing Interesting happened', 'push',action])
#                 else:
#                     player_outcomes.append([hand, dealer_hand, 'Nothing Interesting happened', 'loss',action])
#         else:
#             player_outcomes.append([hand, dealer_hand, 'You Busted', 'loss',action])
#         count = 0
#         for hand in hands:
#             print(hand)
#             for card in hand:
#                 if card in [2,3,4,5,6]:
#                     count += 1
#                 elif card in ['A',10]:
#                     count += (-1)
#                 else:
#                     count += 0
#             print(count)
#         for card in dealer_hand:
#             if card in [2, 3, 4, 5, 6]:
#                 count += 1
#             elif card in ['A', 10]:
#                 count += (-1)
#             else:
#                 count += 0
#     return [player_outcomes,count]

# shoe = bj.create_shoe(6)
# for i in range(20):
#     print(play_round_with_strategy(shoe, True))
# print('complete')



# May need to update shoe as well--need to make a quick test whether this updates an ambient shoe

# def play_shoe_with_strategy(h17):
#     # count = 0
#     shoe = bj.create_shoe(6)
#     outcomes = []
#     while len(shoe) > 15: # and true_count >= -3:
#         x = play_round_with_strategy(shoe,True)
#         # count += x[1]
#         # true_count = count/len(shoe)
#         for outcome in x[0]:
#             outcomes.append(outcome)
#         out_win = []
#         out_loss = []
#         out_push = []
#         out_bj = []
#         out_ddwin = []
#         out_ddloss =[]
#         for outcome in outcomes:
#             if outcome[3]== 'win':
#                 out_win.append(1)
#             if outcome[4] == 'Double Down':
#                 if outcome[3] == 'win':
#                     out_ddwin.append(1)
#                 elif outcome[3] == 'loss':
#                     out_ddloss.append(1)
#             if outcome[2] == 'Blackjack':
#                 out_bj.append(1)
#             elif outcome[3] == 'loss':
#                 out_loss.append(1)
#             elif outcome[3] == 'push':
#                 out_push.append(1)
#     return [outcomes,out_win,out_push,out_loss,out_bj, out_ddloss, out_ddwin]


# def play_shoe_with_strategy_neg_count_leave(h17):
#     count = 0
#     true_count = 0
#     shoe = bj.create_shoe(6)
#     outcomes = []
#     while len(shoe) > 15 and true_count >= -3:
#         x = play_round_with_strategy(shoe,True)
#         count += x[1]
#         true_count = count/len(shoe)
#         for outcome in x[0]:
#             outcomes.append(outcome)
#         out_win = []
#         out_loss = []
#         out_push = []
#         out_bj = []
#         out_ddwin = []
#         out_ddloss =[]
#         for outcome in outcomes:
#             if outcome[3]== 'win':
#                 out_win.append(1)
#             if outcome[4] == 'Double Down':
#                 if outcome[3] == 'win':
#                     out_ddwin.append(1)
#                 elif outcome[3] == 'loss':
#                     out_ddloss.append(1)
#             if outcome[2] == 'Blackjack':
#                 out_bj.append(1)
#             elif outcome[3] == 'loss':
#                 out_loss.append(1)
#             elif outcome[3] == 'push':
#                 out_push.append(1)
#     return [outcomes,out_win,out_push,out_loss,out_bj, out_ddloss, out_ddwin]

def play_shoe_with_count(h17,spread):
    count = 0
    true_count = 0
    shoe = bj.create_shoe(6)
    outcomes = []
    while len(shoe) > 24 and true_count >= -4:
        # bet = 10
        if true_count <= 1:
            bet = 10
        elif true_count >=3:
            bet = 50
        x = play_round_with_strategy(shoe,True)
        count += x[1]
        if len(shoe) >= 52:
            number_decks_left = round(len(shoe)/52)
        else:
            number_decks_left = 1
        true_count = round(count/number_decks_left)
        for outcome in x[0]:
            # print(['count =' + str(count),true_count, bet, len(shoe), bet,outcome])
            outcomes.append(outcome)
        out_win = []
        out_loss = []
        out_push = []
        out_bj = []
        out_ddwin = []
        out_ddloss =[]
        money_won = []
        money_lost = []
        true = []
        # bet = 10
        for outcome in outcomes:
            true.append(true_count)
            if outcome[3] == 'win':
                out_win.append(1)
                money_won.append(bet)
            if outcome[4] == 'Double Down':
                if outcome[3] == 'win':
                    out_ddwin.append(1)
                    money_won.append(bet)
                elif outcome[3] == 'loss':
                    out_ddloss.append(1)
                    money_lost.append(bet)
            if outcome[2] == 'Blackjack':
                out_bj.append(1)
                money_won.append(.5*bet)
            elif outcome[3] == 'loss':
                out_loss.append(1)
                money_lost.append(bet)
            elif outcome[3] == 'push':
                out_push.append(1)

    return [outcomes,out_win,out_push,out_loss,out_bj, out_ddloss, out_ddwin,money_won,money_lost,true]

# for i in range(5):
# shoe = bj.create_shoe(6)
# print(shoe)
# x = play_shoe_with_count(True,6)
# #     for y in x[0]:
# #         print(y)
# print('complete')


def simulate_with_strategy(number_of_shoes,h17,spread):
    hands_won = 0
    hands_lost = 0
    hands_pushed = 0
    blackjacks = 0
    dd_win = 0
    dd_loss = 0
    money_won = 0
    money_lost = 0
    results = []
    for i in range(number_of_shoes):
        x = play_shoe_with_count(True,spread)
        results.append(x)
        hands_won += sum(x[1])
        hands_pushed += sum(x[2])
        hands_lost += sum(x[3])
        blackjacks += sum(x[4])
        dd_win += sum(x[6])
        dd_loss += sum(x[5])
        money_lost += sum(x[8])
        money_won += sum(x[7])

    outcome = dict()
    outcome.update({'Wins':hands_won, 'Losses':hands_lost,'Pushes':hands_pushed, 'Percent Hands Won': hands_won/(hands_won+hands_lost),
                   'Total Number of Hands': hands_won+hands_lost, "number of Blackjacks": blackjacks, "Double Down Win":dd_win,
                    'Double Down Loss': dd_loss})
    outcome.update({'money_won': money_won, 'money_lost':money_lost, 'result': money_won-money_lost, 'percentage_lost':
        100*(money_lost-money_won)/(money_won+money_lost)})
    return [outcome,results]
# total_earnings = 0
# total = 0
# for i in range(100):
x = simulate_with_strategy(1000,True, 12)
#     total += x[0]['result']
#     print(x[0]['result'])
# print('total ='+ str(total))

# for i in [2,3,4,5,6,7,8,9,10,11,12]:
#     x = simulate_with_strategy(1000,True, i)
#     print(x)
#     if x[0]['result'] < 0:
#         print(x[1])
# print(x[1])
    # print(x)
    # total_earnings +=  x['result']
    # print(total_earnings)
# print(x)
print('complete')