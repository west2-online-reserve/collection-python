import random
huases= ['梅花', '方块', '红桃', '黑桃']
zifus= ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
deck = []
def a():
    for huase in huases:
        for zifu in zifus:
            card = huase+zifu
            deck.append(card)
    deck.append("小鬼")
    deck.append("大鬼")
    print(deck)
def b():
    number=random.sample(range(54),54)
    print(number)
    key=0
    for i in number:
        key+=1
        if key<=17:
            with open("player1.txt",'a+',encoding='utf-8')as fp:
                fp.write(deck[i]+'\n')
        elif 17<=key<=34:
            with open("player2.txt",'a+',encoding='utf-8')as fp:
                fp.write(deck[i]+'\n')
        elif 34<=key<=51:
            with open("player3.txt",'a+',encoding='utf-8')as fp:
                fp.write(deck[i]+'\n')
        else:
            with open("others.txt",'a+',encoding='utf-8')as fp:
                fp.write(deck[i]+'\n')
if __name__=="__main__":
    a()
    b()
#github:2877378857qq.com   西二--作业

