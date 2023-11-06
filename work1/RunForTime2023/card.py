# -*- coding: utf-8 -*-
import random
import functools

color = {0: '♠', 1: '♣', 2: '♦', 3: '♥'}
numbers = {0: '3', 1: '4', 2: '5', 3: '6', 4: '7', 5: '8', 6: '9', 7: '10', 8: 'J', 9: 'Q', 10: 'K', 11: 'A', 12: '2'}


def comp(a, b):
    return -1 if (not (a < 52 and b < 52) and a > b) or (
            a < 52 and b < 52 and (a % 13 > b % 13 or (a % 13 == b % 13 and a // 13 > b // 13))) else 1


# 发牌
All = set([i for i in range(54)])
t1 = set(random.sample(All, 17))
t2 = set(random.sample(All - t1, 17))
t3 = set(random.sample(All - t1 - t2, 17))
t4 = set(All - t1 - t2 - t3)
player = [list(t1), list(t2), list(t3), list(t4)]

# 排序+输出
for i in range(4):
    player[i].sort(key=functools.cmp_to_key(comp))
    if (i == 3):
        t = open("others.txt", "w", encoding='utf-8')
    else:
        t = open("player" + str(i + 1) + ".txt", "w", encoding='utf-8')
    for x in player[i]:
        if x == 53:
            t.write("大王 ")
        elif x == 52:
            t.write("小王 ")
        else:
            t.write(numbers[x % 13] + color[x // 13] + ' ')
    t.close()
