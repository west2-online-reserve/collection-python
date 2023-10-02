import random

poke = []
lis1 = tuple(map(lambda l: str(l), range(1, 11))) + ('j', 'q', 'k')
lis2 = ('黑桃', '红桃', '方块', '梅花')
lis3 = tuple(f'player{i+1}' for i in range(3))+('others',)
for i in range(13):
    for j in range(4):
        poke.append({lis2[j] + lis1[i]: i * 4 + j})
poke.extend(({'大王': 52}, {'小王': 53}))
random.shuffle(poke)

new_poke = [[] for i in range(4)]
for i in range(4):
    tem_dic = {}
    if i == 3:
        for j in range(3):
            tem_dic.update(poke[i * 17 + j])
    else:
        for j in range(17):
            tem_dic.update(poke[i * 17 + j])
    new_poke[i] = sorted(tem_dic.items(), key=lambda x: x[1])

for i in range(4):
    with open(f'{lis3[i]}.txt', 'w', encoding='utf-8') as t:
        for j in new_poke[i]:
            t.write(str(j[0]) + '\n')

