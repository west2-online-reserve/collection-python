def listNum(list1):
    d = {}
    for x in list1:
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1
            print(x, d[x])
    return d
def main():
    list1 = [2, 6, 2, 8, 3, 8, 4, 7, 7, 7]
    d = listNum(list1)
    print(d)
if __name__=='__main__':
    main()
