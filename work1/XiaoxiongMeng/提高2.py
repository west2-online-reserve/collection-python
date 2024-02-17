# 发牌系统
from random import randint


def write_down(m, n):
    if 1 <= m <= 17:
        c[m] = 0
        f1.write(n)
    elif 18 <= m <= 34:
        c[m] = 0
        f2.write(n)
    elif 35 <= m <= 51:
        c[m] = 0
        f3.write(n)
    else:
        c[m] = 0
        f.write(n)


a = ["2", "A", 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3']  # 13套牌放进来
b = ['红桃', '黑桃', '方块', '梅花']  # 花色
c = []
for i in range(0, 55):
    c.append(1)
c[0] = 0
f1 = open("D:\\player1.txt", "a", encoding="UTF-8")
f2 = open("D:\\player2.txt", "a", encoding="UTF-8")
f3 = open("D:\\player3.txt", "a", encoding="UTF-8")
f = open("D:\\others.txt", "a", encoding="UTF-8")
ranNum = 0
while c[ranNum] == 0:  # 先分大小王
    ranNum = randint(1, 54)
write_down(ranNum,"大王\n")
while c[ranNum] == 0:  # 先分大小王
    ranNum = randint(1, 54)
write_down(ranNum,"小王\n")
for i in range(0, 13):  # 分其他牌
    for u in range(0, 4):
        ranNum = 0
        while c[ranNum] == 0:
            ranNum = randint(1, 54)
            # 1-17给player1 18-34给player2 35-51给player3 52-54给others
        write_down(ranNum,b[u]+a[i]+"\n")

f1.close()
f2.close()
f3.close()
f.close()
print("发牌完成.请见D盘.若要重新发牌,请删除原有文件.")
