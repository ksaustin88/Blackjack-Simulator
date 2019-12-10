import random

def create_deck():
    deck = []
    for i in range(4):
        for j in range(8):
            deck.append(j+2)
        for j in range(4):
            deck.append(10)
        deck.append('A')
    random.shuffle(deck)
    return deck

def create_shoe(num_of_decks):
    shoe = []
    for i in range(num_of_decks):
        shoe = shoe + create_deck()
    random.shuffle(shoe)
    return shoe

def create_rigged_deck():
    deck = []
    for i in range(4):
        for j in [7,8,9]:
            deck.append(j)
        for j in range(4):
            deck.append(10)
        deck.append('A')
    random.shuffle(deck)
    return deck

def create_rigged_shoe(num_of_decks):
    shoe = []
    for i in range(int(num_of_decks/2)):
        shoe = shoe + create_rigged_deck()
        shoe = shoe + create_deck()
    random.shuffle(shoe)
    return shoe



def hand_count(hand):
    count = [0]
    for card in hand:
        if card in [2,3,4,5,6,7,8,9,10]:
            count = [x+card for x in count]
        if card == 'A':
            count = [int(x+1) for x in count] + [int(x+11) for x in count]
    count = list(set(count))
    new_count = []
    for i in range(len(count)):
        if count[i] <=21:
            new_count.append(count[i])
    return new_count

def hit(shoe,hand):
    hand.append(shoe.pop())
    return hand

def is_soft(hand):
    if len(hand_count(hand)) > 1:
        return True
    else:
        return False
def is_pair(hand):
    if hand[0] == hand[1]:
        return True
    else:
        return False


# x = hand_count(['A',3])
# print('complete')