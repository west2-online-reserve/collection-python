# input函数输入为str类型
def main():
    # 输入列表,使用逗号隔开
    a = input('列表:').split(",")
    for index,element in enumerate(a):
        if (not element.isdigit()):
            a.remove(element)
            # a.pop(index)
            # del a[index]
    a = map(int, a)
    # 默认从小到大排序
    print(sorted(a))
if __name__=='__main__':
    main()
