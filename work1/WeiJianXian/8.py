def fa():
    all = (
        ["A"] * 4
        + ["2"] * 4
        + ["3"] * 4
        + ["4"] * 4
        + ["5"] * 4
        + ["6"] * 4
        + ["7"] * 4
        + ["8"] * 4
        + ["9"] * 4
        + ["10"] * 4
        + ["J"] * 4
        + ["Q"] * 4
        + ["K"] * 4
        + ["joker"]
        + ["JOKER"]
    )
    remain = []
    import random

    random.shuffle(all)  # 打乱

    player1 = all[0:17]  # 切片左闭右开
    player2 = all[17:34]
    player3 = all[34:51]
    remain = all[51:]

    with open("./player1.txt", "w") as f:
        f.write(str(player1))
    with open("./player2.txt", "w") as f:
        f.write(str(player2))
    with open("./player3.txt", "w") as f:
        f.write(str(player3))
    with open("./remain.txt", "w") as f:
        f.write(str(remain))


fa()
