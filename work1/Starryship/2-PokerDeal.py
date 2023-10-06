'''
2.
用所学的知识写一个斗地主随机发牌程序，
将每个人的发牌以及多的三张牌的结果分别按照从大到小的顺序输出到
player1.txt，player2.txt，player3.txt，others.txt四个文件中
'''

from random import shuffle

# 定义玩家
card = [i for i in range(1,55)]
player1 = []
player2 = []
player3 = []
others = []

#打乱牌的顺序
shuffle(card)

# 发牌
i = 0
while (i < 51):
    player1.append(card[i])
    player2.append(card[i + 1])
    player3.append(card[i + 2])
    i += 3
others = card[51:54]

#排序
player1.sort(reverse=True)
player2.sort(reverse=True)
player3.sort(reverse=True)
others.sort(reverse=True)

def Flower(card,i):
    '''判断花色'''
    flower=0
    if card[i]%4==0:
        flower="♠"
    elif card[i]%4==1:
        flower="♦"
    elif card[i]%4==2:
        flower="♣"
    else:
        flower="♥"
    return flower

def changeCard(card):
    '''将数字改为其所代表的牌,按照斗地主中大小排序进行赋值'''
    CardSize = len(card)
    i=0
    for i in range(CardSize):
        if card[i]==53:
            card[i]="joker"  #小王
        elif card[i]==54:
            card[i]="JOKER"  #大王
        elif card[i]<33:
            card[i]=Flower(card,i)+str((card[i]-1)//4+3)
        elif card[i]<53:
            if (card[i]-1)//4 ==8:
                card[i] = Flower(card,i) + "J"
            elif (card[i]-1)//4 ==9:
                card[i] = Flower(card,i) + "Q"
            elif (card[i]-1)//4 ==10:
                card[i] = Flower(card,i) + "K"
            elif (card[i]-1)//4 ==11:
                card[i] = Flower(card,i) + "A"
            elif (card[i]-1)//4 ==12:
                card[i] = Flower(card,i) + "2"
    return card
#使用改变牌号的函数
changeCard(player1)
changeCard(player2)
changeCard(player3)
changeCard(others)

#输出
f1=open("player1",'w',encoding="utf-8")
f1.write(str(player1))
f2=open("player2",'w',encoding="utf-8")
f2.write(str(player2))
f3=open("player3",'w',encoding="utf-8")
f3.write(str(player3))
f4=open("others",'w',encoding="utf-8")
f4.write(str(others))