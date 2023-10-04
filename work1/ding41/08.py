from pathlib import Path
from random import randint

cards=[]
for m in range(4):
    cards.append("J")
    cards.append("K")
    cards.append("Q")
    cards.append("A")
    for i in range(2,11):
        cards.append(str(i))
cards.append("JOKER")
cards.append("joker")

player_1=Path("work1\ding41\player1.txt")
player_2=Path("work1\ding41\player2.txt")
player_3=Path("work1\ding41\player3.txt")
others=Path("work1\ding41\others.txt")

def fapai(text,y):
    t=""
    for w in range(17):
        n=randint(0,y)
        y-=1
        q=cards.pop(n)
        t=t+q+"\n"
    text.write_text(t)

fapai(player_1,53)
fapai(player_2,36)
fapai(player_3,19)

r=""
for e in cards:
    r=r+e+"\n"

others.write_text(r)