import random

g = []      #[0]黑桃，[1]红桃，[2]梅花，[3]方块,[4][0]小王，[4][1]大王
hs = ["黑桃","红桃","梅花","方块","大王","小王"] #花色
nums = []   #点数
play = ["0","player1.txt","player2.txt","player3.txt","others.txt"]
f = [[]]

class poke:
    def __init__(self,ta,sz):
        self.ta = hs[ta]
        self.sz = sz
        self.ch = nums[sz]

def init():
    for i in range(0,10):
      g.append([])
      for j in range(0,20):
         g[i].append(0)
    
    for i in range(0,15+1):
        nums.append(str(int(i)))
    nums[11] = 'J'
    nums[12] = 'Q'
    nums[13] = 'K'
    nums[14] = 'A'
    nums[15] = '2'    
    nums[0] = ''   
 
def work():
    for i in range(1,4+1):
        num = 13
        if(i == 4):
            num = 3
        f.append([])
        f[i].append(poke(0,0))
            
        while num > 0:
            x = random.randint(0,4)   #花色
            if(x <= 3):
                y = random.randint(3,15)  #点数
                #print("x:",x,"y:",y)
            else:
                y = random.randint(0,1) #大小王
                
            if(g[x][y] == 0):
                g[x][y] = 1
                if(x == 4 and y == 0):  #大王
                    f[i].append(poke(4,0))
                elif(x == 4 and y == 1):  #小王
                    f[i].append(poke(5,0))
                else:
                    f[i].append(poke(x,y))  #记录花色，点数
                num -= 1
            else:
                continue
 
def sort(a):
    l = len(a)
    for i in range(1,l-1+1):
        for j in range(i+1,l):
            if(a[i].sz < a[j].sz):
                t = a[i]
                a[i] = a[j]
                a[j] = t
                
                # t = a[i].ta
                # a[i].ta = a[j].ta
                # a[j].ta = t
    return a  
 
if __name__ == "__main__":
    init()
    work()
    for i in range(1,4):
        f[i] = sort(f[i])

    for i in range(1,4+1):
        num = 13
        if(i == 4):
            num = 3
        file = open(play[i],"w+")  #打开文件
        #print("player",i)
        for j in range(1,num+1):
            #print(f[i][j].ta," ",f[i][j].ch)
            file.write(f[i][j].ta+" "+f[i][j].ch+"\n")
        #print("\n")
    