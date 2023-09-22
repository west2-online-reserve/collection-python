# p1
def encslat(temp):#封装
    import time
    def els():
     begin = time.perf_counter()
     temp()
     end = time.perf_counter()
     print(begin)
     print(end)
     print(end-begin)
    return els
@encslat
def func():
    pass
# p2
p={"3":4,"4":4,"5":4,"6":4,"7":4,"8":4,"9":4,"A10":4,"J":4,"Q":4,"_K":4,"c1":4,"c2":4,"joker1-small":1,"joker2-big":1}
pl=[]
for i in p:
   pl.append(i)
pl.sort()
import random
a=[]
b=[]
c=[]
d=[]
t=0
play=[1,2,3]
while len(d)!=3:
    rdo =random.randint(0,14)
    r_num=pl[rdo]
    if p[r_num]==0:
       continue
    p[r_num]-=1
    d.append(r_num)
for i in [a,b,c]:    
    while len(i)!=17:
        rdo =random.randint(0,14)
        r_num=pl[rdo]
        if p[r_num]==0:
           continue
        p[r_num]-=1
        i.append(r_num)
def restore(i):
    i.sort()
    temp=i[::-1]
    temp=str(temp).replace("A10","10")
    temp=temp.replace("_K","K")
    temp=temp.replace("c1","1")
    temp=temp.replace("c2","2")
    return temp
lll=[]
for i in [a,b,c,d]:
   lll.append(restore(i))
for i in range(1,4):
    with open (f"player{i}.txt","w",encoding="utf-8") as f:
        f.write(f"玩家{[i]}的牌是:\n")
        f.write(str(lll[i-1]))
with open ("other_player.txt","w",encoding="utf-8") as f:
   f.write(lll[3])