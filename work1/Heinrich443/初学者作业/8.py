import random
def mywrite(doc, l):
    f = open(doc, 'w+')
    for it in l:
        f.write(it)
        f.write("\n")
    f.close()

cards = ["大王", "小王"]
suits = ["黑桃", "红桃", "方块", "梅花"]
letters = ["A", "J", "Q", "K"]

for suit in suits:
    for i in range(2, 11):
        s = suit + str(i)
        cards.append(s)
    for letter in letters:
        s = suit + letter
        cards.append(s)

random.shuffle(cards)

player1 = cards[0:17]
player2 = cards[17:34]
player3 = cards[34:51]
others = cards[51:]

print(player1)
print(player2)
print(player3)
print(others)

mywrite('player1.txt', player1)
mywrite('player2.txt', player2)
mywrite('player3.txt', player3)
mywrite('others.txt', others)