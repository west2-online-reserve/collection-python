def main():
    for i in range(1, 10):
        for j in range(1, i+1):
            print('%d * %d =%-4d'%(j, i, i * j),end="")
            # print(f'{i}*{j}={i*j}',end=" ")
        print()
if __name__=='__main__':
    main()
