#尝试用所学的知识写一个斗地主随机发牌程序，
# 将每个人的发牌以及多的三张牌的结果分别输出到player1.txt，player2.txt，player3.txt，others.txt四个文件中，可以不要求牌的花色
import random
from typing import List

player1=[]
player2=[]
player3=[]
others=[]
card = []
for i in range(1, 14):
    for x in range(4):
        card.append(i)
card.append(14)#大王
card.append(15)#小王
for i in range(10):
    random.shuffle(card)
i=0
while i<51:
    player1.append(card[i])
    player2.append(card[i+1])
    player3.append(card[i+2])
    i=i+3
others.append(card[51])
others.append(card[52])
others.append(card[53])
player1.sort()
player2.sort()
player3.sort()#理牌
for i in range(17):
    if player1[i] == 1:
        player1[i] = "A"
    elif player1[i] == 11:
        player1[i] = "J"
    elif player1[i] == 12:
        player1[i] = "Q"
    elif player1[i] == 13:
        player1[i] = "K"
    elif player1[i] == 14:
        player1[i] = "JOKER"
    elif player1[i] == 15:
        player1[i] = "joker"
    if player2[i] == 1:
        player2[i] = "A"
    elif player2[i] == 11:
        player2[i] = "J"
    elif player2[i] == 12:
        player2[i] = "Q"
    elif player2[i] == 13:
        player2[i] = "K"
    elif player2[i] == 14:
        player2[i] = "JOKER"
    elif player2[i] == 15:
        player2[i] = "joker"
    if player3[i] == 1:
        player3[i] = "A"
    elif player3[i] == 11:
        player3[i] = "J"
    elif player3[i] == 12:
        player3[i] = "Q"
    elif player3[i] == 13:
        player3[i] = "K"
    elif player3[i] == 14:
        player3[i] = "JOKER"
    elif player3[i] == 15:
        player3[i] = "joker"
for i in range(3):
    if others[i] == 1:
        others[i] = "A"
    elif others[i] == 11:
        others[i] = "J"
    elif others[i] == 12:
        others[i] = "Q"
    elif others[i] == 13:
        others[i] = "K"
    elif others[i] == 14:
        others[i] = "JOKER"
    elif others[i] == 15:
        others[i] = "joker"
p1=open("player1.txt","w")
p1.writelines(str(player1))
p2=open("player2.txt","w")
p2.writelines(str(player2))
p3=open("player3.txt","w")
p3.writelines(str(player3))
o=open("others.txt","w")
o.writelines(str(others))


