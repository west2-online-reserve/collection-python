import random
global dizhu
def wrichangestr(a):
    b=""
    for i in a:
        b=b+i+"  "
    return b
def FAPAI():

    
    b=["2","3","4","5","6","7","8","9","10","J","K","Q","A"]
    c=["梅花","方块","红桃","黑桃"]
    a=[]
    player=[1,2,3]
    player_=[1,2,3]
    dizhu=0
    pingming=[]
    for i in c:
        for j in b:
         a.append(i+j)#列表a存放所有牌
    dizhu=0

    flag=0
    while True:
        random.shuffle(a)
        for i in range(1,4):
            print("是否选择叫地主,请回答是或不是")
            choice=input()
            if choice=="是":
                dizhu=i
                flag=1
            if flag==1:
                break
        break
    player.pop(dizhu-1)


    for i in player:
        print("是否抢地主")
        choice1=input("回答是或不是\n")
        if choice1=="是":
            dizhu=i
    print("地主是",dizhu)
    player_.pop(dizhu-1)
    for i in player_:
        print("农民是",i)
    
    p="player"
    for i in player_:
        pingming.append("player"+str(i))
    
    for i in range(len(pingming)):
        t=open(pingming[i]+".txt","w+",encoding="utf-8")
        t.write(wrichangestr(a[i*17:i*17+17]))
        t.close()
    p=open("player"+str(dizhu)+".txt","w+",encoding="utf-8")
    p.write(wrichangestr(a[34::]))
    p.close()

FAPAI()