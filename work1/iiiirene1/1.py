#输入三个整数x,y,z，请尝试用多种方式把这三个数由大到小输出
x = int(input('第一个整数x：'))
y = int(input('第二个整数x：'))
z = int(input('第三个整数x：'))
# f方法1
max = x
if y > x:
    if y > z:
        max = y
        y = x
        x = max
        if z > y:
            max = z
            z = y
            y = max
    elif z > y:
        max = z
        z = x
        x = max
else:
    if z > x:
        max = z
        z = x
        x = max
        if z > y:
            max = z
            z = y
            y = max
    else:
        if z > y:
            max = z
            z = y
            y = max
print(x, y, z)

# 方法2
if y > x:
    if z > y:
        z, x = x, z
    else:
        if x > z:
            y, x = x, y
        else:
            x, y, z = y, z, x
else:
    if z > x:
        x, y, z = z, x, y
    else:
        if z > y:
            z, y = y, z
print(x, y, z)


# 方法3
if y > x:
    x, y = y, x
if z > x:
    x, z = z, x
if z > y:
    y, z = z, y

print(x, y, z)

#方法4
List = [x, y, z]
List = sorted(List,reverse=True) #sorted可实现对可迭代对象进行排序，其中reverse参数默认为False，实现由小到大排序，此处需要实现由大到小排序，故需把此参数值赋值为True
print(List)
#-------------------------------------------------------------------------------------------------------------------------------------
#2.输出九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print("{} * {} = {}".format(j,i,j*i),end=' ')
    print()
#---------------------------------------------------------------------------------------------------------------------------------------
#3. 输入⼀个字符串，判断字符串中是否含有"ol"这个⼦串，若有把所有的"ol"替换为"fzu"，最后把字符串倒序输出
a="ol"
string = str(input("Please input a string："))
if a in string:
    string.replace(a,"fzu")
    print(string[::-1])
else:
    print("No")
  #---------------------------------------------------------------------------------------------------------------------------------------
  #4. 输入⼀个列表（list），列表中含有字符串和整数，删除其中的字符串元素，然后把剩下的整数升序排序，输出列表
lst=list(input("输入元素，并用英文逗号隔开：").split(','))
for item in lst:
    if type(item) == str:
        lst.remove(item)
lst.sort()
print(lst)
#---------------------------------------------------------------------------------------------------------------------------------------

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

#---------------------------------------------------------------------------------------------------------------------------------------
#创建一个函数，这个函数可以统计一个只有数字的列表中各个数字出现的次数，通过字典方式返回


l1= map(float, input("输入数字元素，并用,隔开：").split(','))
dict = {}
for i in l1:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1
print(dict)

#---------------------------------------------------------------------------------------------------------------------------------------
#7设计⼀个商品类，它具有的私有数据成员是商品序号、商品名、单价、总数量和剩余数量。具有的 公有成员函数是：初始化商品信息的构造函数__init__，显示商品信息的函数display，计算已售出 商品价值income，修改商品信息的函数setdata

class Goods:
    def __init__(self,no,name,price=0,total=0,spare=0):
        self.no = no
        self.name = name
        self.price = int(price)
        self.total = int(total)
        self.spare = int(spare)

class GoodsList:
    def __init__(self):
        self.gdslist = []

    def display(self):
        # 显示信息
        print('{}\t{}\t{}\t{}\t{}\t{}'
              .format('商品序号', '商品名', '单价', '总数量', '剩余数量'))
        for gd in self.gdslist:
            print('{}\t{}\t{}\t{}\t{}'
                  .format(gd.no, gd.name, gd.price, gd.total, gd.spare))

    def setdata(self):
        # 删除信息
        while True:
            no = input('请输入要删除的商品编号:')
            for gd in self.gdslist[::]:
                if gd.no == no:
                    self.gdslist.remove(gd)
                    print('删除成功')
                    break
            else:
                print('该编号不存在')
            choice = input('继续删除(y/n)?').lower()
            if choice == 'n':
                break
    def incomecal(self):
        while True:
            for gd in self.gdslist:
                income = [gd.total - gd.spare]*gd.price
                print(income)


