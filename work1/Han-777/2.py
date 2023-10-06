# 用所学的知识写一个斗地主随机发牌程序，将每个人的发牌以及多的三张牌的结果分别
# 按照从大到小的顺序输出到player1.txt，player2.txt，player3.txt，others.txt四个文件中
#
import random


class Poke:
    __flowers = ["♦", "♣", "♥", "♠"]
    __numbers = ["3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "2"]
    __king = {'小王': 100, '大王': 200}
    poke = []
    player1 = []
    player2 = []
    player3 = []
    rest = None
    ll = None

    def __init__(self, flowers, numbers):
        self.flower = flowers
        self.number = numbers

    def __str__(self):
        return f"{self.flower}{self.number} "  # output a string for the class was called

    @classmethod
    def pokeInit(cls):
        cls.poke = [flower + number for flower in cls.__flowers for number in cls.__numbers]
        for key in list(cls.__king.keys()):
            cls.poke.append(key)

    print("welcome to Poke game".center(100, "-"))

    @classmethod
    def shufflePoke(cls):
        random.shuffle(cls.poke)

    @classmethod
    def LandlordCard(cls):
        cls.ll = random.choice(cls.poke)
        print(f"Landlord card: {cls.ll}")

    @classmethod
    def deal(cls):
        for card in range(17):
            cls.player1.append(cls.poke.pop(0))
            cls.player2.append(cls.poke.pop(0))
            cls.player3.append(cls.poke.pop(0))
        cls.rest = list(cls.poke)
        cls.pokeSort(cls.player1)
        cls.pokeSort(cls.player2)
        cls.pokeSort(cls.player3)
        cls.pokeSort(cls.rest)

    @classmethod
    def pokeSort(cls, listName):
        if cls.ll in listName:
            for card in cls.rest:
                listName.append(card)

        n = len(listName)
        kingFlag = 0
        smallIndex = -1
        bigIndex = -1
        # sort king
        for card in list(cls.__king.keys()):
            if card in listName:
                if card == list(cls.__king.keys())[0]:
                    smallIndex = listName.index(card)
                    kingFlag += 1
                elif card == list(cls.__king.keys())[1]:
                    bigIndex = listName.index(card)
                    kingFlag += 1

        if kingFlag == 2:
            listName[smallIndex], listName[n - 2] = listName[n - 2], listName[smallIndex]
            listName[bigIndex], listName[n - 1] = listName[n - 1], listName[bigIndex]
        elif kingFlag == 1:
            cardIndex = smallIndex if smallIndex != -1 else bigIndex
            listName[cardIndex], listName[n - 1] = listName[n - 1], listName[cardIndex]
        # sort number
        for i in range(n):
            for j in range(n - i - 1 - kingFlag):
                if cls.__numbers.index(listName[j][1:]) > cls.__numbers.index(listName[j + 1][1:]):
                    listName[j], listName[j + 1] = listName[j + 1], listName[j]
                # sort flower
                elif cls.__numbers.index(listName[j][1:]) == cls.__numbers.index(listName[j + 1][1:]):
                    if cls.__flowers.index(listName[j][0:1]) > cls.__flowers.index(listName[j + 1][0:1]):
                        listName[j], listName[j + 1] = listName[j + 1], listName[j]

        cls.inputFile(cls.player1, "player1.txt")
        cls.inputFile(cls.player2, "player2.txt")
        cls.inputFile(cls.player3, "player3.txt")
        cls.inputFile(cls.rest, "others.txt")

    @classmethod
    def inputFile(cls, playerList, fileName):
        file = open(f"{fileName}", "w+", encoding='utf-8')
        for card in reversed(playerList):
            file.write(card)
            file.write(" ")
        file.close()

    @classmethod
    def grabLandlord(cls, playerNum, playerList):
        print(f"player{playerNum} ==>>", end=' ')
        if cls.ll in playerList:
            print("Landlord")
        else:
            print("farmer")
        for card in reversed(playerList):
            print(card, end=' ')
        print()

    @classmethod
    def printInfo(cls):
        print("rest card:")
        for card in reversed(cls.rest):
            print(card, end=' ')
        print()
        cls.grabLandlord(1, cls.player1)
        cls.grabLandlord(2, cls.player2)
        cls.grabLandlord(3, cls.player3)
        print("game begin".center(100, "-"))


Poke.pokeInit()
Poke.shufflePoke()
Poke.LandlordCard()
Poke.deal()
Poke.printInfo()
