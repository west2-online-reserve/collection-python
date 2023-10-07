import random


def deal_cards():
    suits = ['♦', '♣', '♥', '♠']
    values = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2']
    special_cards = ['Joker1', 'Joker2']
    cards = [value + suit for suit in suits for value in values] + special_cards
    random.shuffle(cards)

    def sort_key(card):
        if card in special_cards:
            return (14 + special_cards.index(card), -1)
        return (values.index(card[:-1]), suits.index(card[-1]))

    player1 = sorted(cards[:17], key=sort_key, reverse=True)
    player2 = sorted(cards[17:34], key=sort_key, reverse=True)
    player3 = sorted(cards[34:51], key=sort_key, reverse=True)
    others = sorted(cards[51:], key=sort_key, reverse=True)

    with open("player1.txt", "w", encoding="utf-8") as f1, open("player2.txt", "w", encoding="utf-8") as f2, open(
            "player3.txt", "w", encoding="utf-8") as f3, open("others.txt", "w", encoding="utf-8") as f4:
        f1.write("\n".join(player1))
        f2.write("\n".join(player2))
        f3.write("\n".join(player3))
        f4.write("\n".join(others))


deal_cards()
