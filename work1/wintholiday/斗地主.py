import random

def generate_poker():

    poker = []
    colors = ['♥', '♠', '♣', '♦']
    for color in colors:
        for i in range(3, 11):
            poker.append(color + str(i))
        poker.append(color + '2')
        poker.append(color + 'A')
        poker.append(color + 'J')
        poker.append(color + 'Q')
        poker.append(color + 'K')
    poker.append('小王')
    poker.append('大王')
    return poker

def send(poker):
    random.shuffle(poker)
    player1 = poker[:17]
    player2 = poker[17:34]
    player3 = poker[34:51]
    others = poker[51:]
    return player1, player2, player3, others

def sort(poker):
    # 按照从大到小排序
    def poker_key(card):
        if card == '大王':
            return 17
        elif card == '小王':
            return 16

        else:
            face = card[1:]
            if face == '2':
                return 15
            elif face.isdigit():
                return int(face)
            elif face == 'A':
                return 14

            elif face == 'J':
                return 11
            elif face == 'Q':
                return 12
            elif face == 'K':
                return 13
        return 0
    return sorted(poker, key=poker_key, reverse=True)

def write(filename, poker):
    with open(filename, 'w') as f:
        f.write(' '.join(sort(poker)))

if __name__ == '__main__':
    poker = generate_poker()
    player1, player2, player3, others = send(poker)
    write('player1.txt', player1)
    write('player2.txt', player2)
    write('player3.txt', player3)
    write('others.txt', others)
