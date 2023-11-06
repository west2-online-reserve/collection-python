#5. 创建一个字典（dict），为字典添加几个键为学号，值为姓名元素，删除学号尾号为偶数的元素，输出字典
dic = {}
i=1
while i >0:
    num = (input("请输入学生学号(输入q停止输入信息)："))
    if num == 'q':
        break
    if num in dic.keys():
        print("已存在,请重新输入")
    elif num == 0:
        break
    else:
        name = input("请输入学生姓名：")
        dic[num]= name   #向字典中添加元素
#以上是字典的输入

list1= list(dic.keys())  #将字典里的key值生成列表
for key in range(len(list1)):
    if key%2==0:
        del dic[key]
        continue
print(dic)

