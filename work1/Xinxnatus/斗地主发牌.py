import random

def shuffle(Poker):
    player1, player2, player3, others = [], [], [], []
    Poker_copy = Poker.copy()
    for i in range(17):
        for player in [player1, player2, player3]:
            r = Poker_copy.pop(random.randint(0, len(Poker_copy)-1))
            player.append(r)

    others = Poker_copy
    return player1, player2, player3, others


def sort_player(player):
    order = {'3': 0, '4': 1, '5': 2, '6': 3, '7': 4, '8': 5, '9': 6, '10': 7, 'J': 8, 'Q': 9, 'K': 10, 'A': 11, '2': 12, 'Little King': 13, 'Big King': 14}
    sorted_player = sorted(player, key=lambda n: order[n])
    return sorted_player


def save(player,filename):
    with open(filename, 'w') as file:
        for i in player:
            file.write(f'{i}  ')


Poker = (list('23456789JQKA') + ['10']) * 4 + ['Big King', 'Little King']
player1, player2, player3, others = shuffle(Poker)
player1 = sort_player(player1)
player2 = sort_player(player2)
player3 = sort_player(player3)
others = sort_player(others)

print(player1)
save(player1,'player1.txt')
print(player2)
save(player2,'player2.txt')
print(player3)
save(player3,'player3.txt')
print(others)
save(others,'others.txt')


