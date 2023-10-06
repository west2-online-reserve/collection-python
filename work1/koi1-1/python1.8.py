import random
deck = [i for i in range(1, 55)]
random.shuffle(deck)
player1 = deck[:17]
player2 = deck[17:34]
player3 = deck[34:51]
others = deck[51:]
with open("player1.txt", "w") as file1:
    for card in player1:
        file1.write(str(card) + " ")
with open("player2.txt", "w") as file2:
    for card in player2:
        file2.write(str(card) + " ")
with open("player3.txt", "w") as file3:
    for card in player3:
        file3.write(str(card) + " ")
with open("others.txt", "w") as file4:
    for card in others:
        file4.write(str(card) + " ")
print("发牌完成，并已写入到四个文件中：player1.txt, player2.txt, player3.txt, others.txt")
