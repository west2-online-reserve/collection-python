from random import choice

card_color = ["hearts", "diamonds", "clubs", "spades"]
card_number = ["K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2", "A"]
king_card = ["big joker", "little jorker"]
f1 = open("./player1.txt", "w", encoding="utf-8")
f2 = open("./player2.txt", "w", encoding="utf-8")
f3 = open("./player3.txt", "w", encoding="utf-8")
f4 = open("./others.txt", "w", encoding="utf-8")
list1 = [f1, f2, f3, f4]
set = [0, 1, 2, 3]
a = 0
b = 0
c = 0
d = 0
for i in range(len(king_card)):
    num = choice(set)
    list1[num].write(f" {king_card[i]}\n")
    if num == 0:
        a += 1
    if num == 1:
        b += 1
    if num == 2:
        c += 1
    if num == 3:
        d += 1
    # 先发大小王

for i in range(len(card_number)):
    for j in range(len(card_color)):
        num = choice(set)
        list1[num].write(f" {card_number[i]} {card_color[j]}\n")
        if num == 0:
            a += 1
        if num == 1:
            b += 1
        if num == 2:
            c += 1
        if num == 3:
            d += 1
        if a >= 17:
            set.remove(0)
            a = 0
        if b >= 17:
            set.remove(1)
            b = 0
        if c >= 17:
            set.remove(2)
            c = 0
        if d >= 3:
            set.remove(3)
            d = 0
        # 将牌从大到小排列并随机发给一名角色
        # 通过abcd这四个变量统计玩家抽取的牌数，使得手牌数符合要求

f1.close()
f2.close()
f3.close()
f4.close()
