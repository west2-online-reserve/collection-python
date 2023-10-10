import random
def daozhi(a):
    if type(a)!=list:
        print("倒了几次，醉成这样")
        return None
    else:
        for i in a:
            if type(i)!=list:
                return "这也能倒?"
    return [list(j) for j in zip(*a)]
print("你要生成几行几列的矩阵")
Ind=int(input("行数是"))
Clo=int(input("列数是"))
list1=[[random.randint(0,100) for i in range(Clo)] for j in range(Ind) ]
print(daozhi())

'''


a=[[1 for i in range(5)] for j in range(10) ]
  
b=map(lambda x:map(lambda y:y+2,x),a)
print(list(list(b)))

matrix = [[1, 2, 3], [4, 5, 6]]
transposed_matrix = [list(col) for col in zip(*matrix)]
print(transposed_matrix)  # 输出: [[1, 4], [2, 5], [3, 6]]



'''