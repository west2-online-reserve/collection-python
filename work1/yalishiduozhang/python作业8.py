import random
#生成一副乱序牌
def generate_decks():
    deck = ['1','2','3','4','5','6','7','8','9','J','Q','K','A']
    decks = [rank for rank in deck for i in range(4)]
    decks.append('小王')
    decks.append('大王')
    random.shuffle(decks)
    return decks
# print(generate_decks())

#发牌
def send_cards(decks):
    players=[[],[],[]]
    others=[]
    for i ,card in enumerate(decks):
        n = i % 3
        players[n].append(card)
    others=decks[-3:]
    return players,others

# deck = generate_decks()
# print(send_cards(deck))

#输出
def save(players,others):
    with open('player1.txt','w') as file:
        file.write(' '.join(players[0]))
    with open('player2.txt', 'w') as file:
        file.write(' '.join(players[1]))

    with open('player3.txt', 'w') as file:
        file.write(' '.join(players[2]))

    with open('others.txt', 'w') as file:
        file.write(' '.join(others))

if __name__ == '__main__':
    decks = generate_decks()
    players,others=send_cards(decks)
    save(players,others)


