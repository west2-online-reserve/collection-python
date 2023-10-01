for x in range(1, 10):
    for y in range(1, 10):
        if x >= y:
            print(f"{x} x {y} = {x*y}", end=" ")  # 清除掉print自带的换行
    print("")  # 因为print末尾自带一个换行，所以换行只需要print("")
