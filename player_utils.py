import BJ_utils as bj

# def hard(shoe,hand,dealer_hand):
#     if len(bj.hand_count(hand)) >0:
#         dealer_card = dealer_hand[1]
#         if dealer_card == 'A':
#             dealer_card = 11
#         elif 4 <= max(bj.hand_count(hand)) <= 8:
#             hand = bj.hit(shoe,hand)
#             return [hand, 'continue']
#         elif len(hand) == 2 and max(bj.hand_count(hand)) ==9 and 3 <= dealer_card and dealer_card <= 6:
#             hand = bj.hit(shoe,hand)
#             return [hand,'Double Down']
#         elif len(hand) >= 2 and max(bj.hand_count(hand)) ==9:
#             hand = bj.hit(shoe,hand)
#             return [hand, 'continue']
#         elif len(hand) == 2 and max(bj.hand_count(hand)) ==10 and 2 <= dealer_card and dealer_card <= 9:
#             return [bj.hit(shoe,hand),'Double Down']
#         elif len(hand) >= 2 and max(bj.hand_count(hand)) ==10:
#             hand = bj.hit(shoe,hand)
#             return [hand, 'continue']
#         elif len(hand) == 2 and max(bj.hand_count(hand)) ==11:
#             return [bj.hit(shoe,hand),'Double Down']
#         elif len(hand) >= 2 and max(bj.hand_count(hand)) == 11:
#             hand = bj.hit(shoe,hand)
#             return [hand, 'continue']
#         elif max(bj.hand_count(hand)) ==12 and 4 <= dealer_card and dealer_card <=6:
#             return [hand,'stay']
#         elif max(bj.hand_count(hand)) == 12:
#             hand = bj.hit(shoe,hand)
#             return [hand, 'continue']
#         elif max(bj.hand_count(hand)) in [13,14,15,16]  and dealer_card <=6:
#             return [hand,'stay']
#         elif max(bj.hand_count(hand)) in [13,14,15,16]:
#             hand = bj.hit(shoe,hand)
#             return [hand, 'continue']
#         elif max(bj.hand_count(hand)) == 17 and dealer_card ==11:
#             hand = bj.hit(shoe,hand)
#             return [hand, 'continue']
#         elif max(bj.hand_count(hand)) >= 17:
#             return [hand, 'stay']
#         else:
#             return [hand,'stay']
#     else:
#         return [hand,'You Lost']

def hard(shoe,hand,dealer_hand,count):
    if len(bj.hand_count(hand)) >0:
        dealer_card = dealer_hand[1]
        if dealer_card == 'A':
            dealer_card = 11
        if 4 <= max(bj.hand_count(hand)) <= 8:
            hand = bj.hit(shoe,hand)
            return [hand, 'continue']
        elif len(hand) == 2 and max(bj.hand_count(hand)) ==9 and 3 <= dealer_card and dealer_card <= 6:
            hand = bj.hit(shoe,hand)
            return [hand,'Double Down']
        elif len(hand) >= 2 and max(bj.hand_count(hand)) ==9:
            hand = bj.hit(shoe,hand)
            return [hand, 'continue']
        elif len(hand) == 2 and max(bj.hand_count(hand)) ==10 and 2 <= dealer_card and dealer_card <= 9:
            return [bj.hit(shoe,hand),'Double Down']
        elif len(hand) >= 2 and max(bj.hand_count(hand)) ==10:
            hand = bj.hit(shoe,hand)
            return [hand, 'continue']
        elif len(hand) == 2 and max(bj.hand_count(hand)) ==11:
            return [bj.hit(shoe,hand),'Double Down']
        elif len(hand) >= 2 and max(bj.hand_count(hand)) == 11:
            hand = bj.hit(shoe,hand)
            return [hand, 'continue']
        elif max(bj.hand_count(hand)) ==12 and 4 <= dealer_card and dealer_card <=6:
            return [hand,'stay']
        elif max(bj.hand_count(hand)) == 12:
            hand = bj.hit(shoe,hand)
            return [hand, 'continue']
        elif max(bj.hand_count(hand)) in [13,14,15,16]  and dealer_card <=6:
            return [hand,'stay']
        elif max(bj.hand_count(hand)) in [13,14,15,16]:
            hand = bj.hit(shoe,hand)
            return [hand, 'continue']
        elif max(bj.hand_count(hand)) == 17 and dealer_card ==11:
            hand = bj.hit(shoe,hand)
            return [hand, 'continue']
        elif max(bj.hand_count(hand)) >= 17:
            return [hand, 'stay']
        else:
            return [hand,'stay']
    else:
        return [hand,'You Lost']

# def soft(shoe, hand, dealer_hand):
#     dealer_card = dealer_hand[1]
#     if dealer_card == 'A':
#         dealer_card = 11
#     if len(bj.hand_count(hand)) > 0:
#         if len(hand) == 2 and max(bj.hand_count(hand)) in [12, 13, 14] and dealer_card in [5, 6]:
#             return [bj.hit(shoe, hand), 'Double Down']
#         elif len(hand) >= 2 and max(bj.hand_count(hand)) in [12, 13, 14]:
#             hand = bj.hit(shoe, hand)
#             return [hand, 'continue']
#         elif len(hand) == 2 and max(bj.hand_count(hand)) in [15, 16] and dealer_card in [4, 5, 6]:
#             return [bj.hit(shoe, hand), 'Double Down']
#         elif len(hand) >= 2 and max(bj.hand_count(hand)) in [15, 16]:
#             hand = bj.hit(shoe, hand)
#             return [hand, 'continue']
#         elif len(hand) == 2 and max(bj.hand_count(hand)) == 17 and dealer_card in [3, 4, 5, 6]:
#             return [bj.hit(shoe, hand), 'Double Down']
#         elif len(hand) >= 2 and max(bj.hand_count(hand)) == 17:
#             hand = bj.hit(shoe, hand)
#             return [hand, 'continue']
#         elif len(hand) == 2 and max(bj.hand_count(hand)) == 18 and dealer_card in [2, 3, 4, 5, 6]:
#             return [bj.hit(shoe, hand), 'Double Down']
#         elif len(hand) >= 2 and max(bj.hand_count(hand)) == 18 and dealer_card >= 9:
#             hand = bj.hit(shoe, hand)
#             return [hand, 'continue']
#         elif len(hand) >= 2 and max(bj.hand_count(hand)) == 18 and dealer_card <= 8:
#             return [hand, 'stay']
#         elif len(hand) == 2 and max(bj.hand_count(hand)) == 19 and dealer_card == 6:
#             return [bj.hit(shoe, hand), 'Double Down']
#         elif len(hand) >= 2 and max(bj.hand_count(hand)) == 19:
#             return [hand, 'stay']
#         elif max(bj.hand_count(hand)) >= 20:
#             return [hand, 'stay']
#         else:
#             return [hand, 'stay']
#     else:
#         return [hand, 'You Lost']
# # shoe = bj.create_shoe(6)
# # x = hard(shoe, ['A',3], [4,2])
# # print('compltr')
#
# #need to have an output for when the shoe doesnt have enough cards
# ## Just the Basic Strategy Points. Eventually incorperate the count into things
def play_strategy(shoe,hand,dealer_hand,count):
    if len(bj.hand_count(hand[0])) == 0:
        return [hand[0],'stay']
    else:
        if hand == None:
            return [hand,'stay']
        if hand[1] == 'Double Down':
            return [hand[0], 'Double Down']
        if hand[1] == 'stay':
            return [hand[0], 'stay']
        elif hand[1] == 'continue':
            dense = bj.is_soft(hand[0])
            if dense == True:
                hand = soft(shoe,hand[0],dealer_hand,count)
                return play_strategy(shoe,hand,dealer_hand,count)
            else:
                hand = hard(shoe,hand[0],dealer_hand,count)
                return play_strategy(shoe,hand,dealer_hand,count)

def soft(shoe,hand,dealer_hand,count):
    if len(bj.hand_count(hand)) >0:
            dealer_card = dealer_hand[1]
            if dealer_card == 'A':
                dealer_card = 11
            if len(hand) == 2 and max(bj.hand_count(hand)) in [12,13,14] and dealer_card in [5,6]:
                return [bj.hit(shoe,hand),'Double Down']
            elif len(hand) >= 2 and max(bj.hand_count(hand)) in [12,13,14]:
                hand = bj.hit(shoe,hand)
                return [hand,'continue']
            elif len(hand) == 2 and max(bj.hand_count(hand)) in [15,16] and dealer_card in [4,5,6]:
                return [bj.hit(shoe,hand),'Double Down']
            elif len(hand) >= 2 and max(bj.hand_count(hand)) in [15,16]:
                hand = bj.hit(shoe,hand)
                return [hand,'continue']
            elif len(hand) == 2 and max(bj.hand_count(hand)) ==17 and dealer_card in [3,4,5,6]:
                return [bj.hit(shoe,hand),'Double Down']
            elif len(hand) >= 2 and max(bj.hand_count(hand)) == 17:
                hand = bj.hit(shoe,hand)
                return [hand,'continue']
            elif len(hand) == 2 and max(bj.hand_count(hand)) ==18 and dealer_card in [2,3,4,5,6]:
                return [bj.hit(shoe,hand),'Double Down']
            elif len(hand) >= 2 and max(bj.hand_count(hand)) == 18 and dealer_card >= 9:
                hand = bj.hit(shoe,hand)
                return [hand,'continue']
            elif len(hand) >= 2 and max(bj.hand_count(hand)) == 18 and dealer_card <=8:
                return [hand,'stay']
            elif len(hand) == 2 and max(bj.hand_count(hand)) ==19 and dealer_card ==6:
                return [bj.hit(shoe,hand),'Double Down']
            elif len(hand) >= 2 and max(bj.hand_count(hand)) == 19:
                return [hand,'stay']
            elif max(bj.hand_count(hand)) >= 20:
                return [hand,'stay']
    else:
        return [hand,'You Lost']

def splitter(shoe,hands,dealer_card):
    old_hands = hands
    new_hands = []
    for hand in old_hands:
        if bj.is_pair(hand) == True:
            if hand[0] in ['A',8]:
                hand_0 = [hand[0]]
                hand_1 = [hand[1]]
                hand_0.append(shoe.pop())
                hand_1.append(shoe.pop())
                new_hands.append(hand_0)
                new_hands.append(hand_1)
            elif hand[0] in [10,5]:
                new_hands.append(hand)
            elif hand[0] == 9 and dealer_card not in [7,10,'A']:
                    hand_0 = [hand[0]]
                    hand_1 = [hand[1]]
                    hand_0.append(shoe.pop())
                    hand_1.append(shoe.pop())
                    new_hands.append(hand_0)
                    new_hands.append(hand_1)
            elif hand[0] == 7 and dealer_card not in [8,9,10,'A']:
                hand_0 = [hand[0]]
                hand_1 = [hand[1]]
                hand_0.append(shoe.pop())
                hand_1.append(shoe.pop())
                new_hands.append(hand_0)
                new_hands.append(hand_1)
            elif hand[0] == 6 and dealer_card not in [7,8,9,10,'A']:
                hand_0 = [hand[0]]
                hand_1 = [hand[1]]
                hand_0.append(shoe.pop())
                hand_1.append(shoe.pop())
                new_hands.append(hand_0)
                new_hands.append(hand_1)
            elif hand[0] == 4 and dealer_card in [5,6]:
                hand_0 = [hand[0]]
                hand_1 = [hand[1]]
                hand_0.append(shoe.pop())
                hand_1.append(shoe.pop())
                new_hands.append(hand_0)
                new_hands.append(hand_1)
            elif hand[0] in [2,3] and dealer_card in [2,3,4,5,6,7]:
                hand_0 = [hand[0]]
                hand_1 = [hand[1]]
                hand_0.append(shoe.pop())
                hand_1.append(shoe.pop())
                new_hands.append(hand_0)
                new_hands.append(hand_1)
            else:
                new_hands.append(hand)
        else:
            new_hands = old_hands
    return new_hands

# shoe = bj.create_shoe(6)
# print(shoe)
# x = splitter(shoe,[[2,4]], [4,'A'])
# print('complete')


# shoe = bj.create_shoe(6)
# print(shoe)
# print(play_strategy(shoe,[[2,3],'continue'], [3,9]))
# print('complete')