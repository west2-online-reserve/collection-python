import random
dic={}
for i in range(1,14):
    dic['%s'%(i)]=4
dic['14']=1
dic['15']=1
i=0
a=[]
b=[]
c=[]
d=[a,b,c]
dicp={'12':'A','13':'2','1':'3','2':'4','3':'5','4':'6','5':'7','6':'8','7':'9','8':'10','9':'J','10':'Q','11':'K','14':'小王','15':'大王'}
while i<51:
    for r in d:
        flag=1
        while flag:
            n=random.randint(1,15)
            if dic[str(n)]>0:
                r.append(n)
                dic[str(n)]-=1
                flag=0
                i+=1
for j in range(len(d)):
    r=d[j]
    with open('play%d'%(j+1)+'.txt','w',encoding='utf8') as f:
        r.sort()
        for t in range(len(r)):
            r[t]=dicp[str(r[t])]
            f.write(' '+r[t])
with open('other.txt','w',encoding='utf8')as p:
    for k in dic:
        while dic[k]!=0:
            p.write(' '+dicp[k])
            dic[k]-=1





