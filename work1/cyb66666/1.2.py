#输入三个整数x,y,z，请尝试用多种方式把这三个数由大到小输出
a,b,c=input().split()
n=[a,b,c]
n.sort(reverse=True)
print(n)