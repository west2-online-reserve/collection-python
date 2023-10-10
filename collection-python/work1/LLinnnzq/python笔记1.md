# python笔记

### bool与逻辑判断

`a = True
b = not a
print(b)
print(not b)
print(a == b)
print(a != b)
print(a and b)
print(a or b)
print(1 < 2 and b==True)`

结果如下

`False
True
False
True
False
True
False`

**not** x为True,则not x为False

**and** x,y中至少一个False，结果为False

**or** x,y中至少一个True,则x or y为True

**NOT OR**

not (True or False) <=> False

not (True or True) <=> False

not (False or True) <=> False

not (False or False) <=> True

**NOT AND**

not (True and False) <=> True

not (True and True) <=> False

not (False and True) <=> True

not (False and False) <=> True

**!=**

1 != 0 <=> True

1 != 1 <=> False

0 != 1 <=> True

0 != 0 <=> False

**==**

1 == 0 <=> False

1 == 1 <=> True

0 == 1 <=> False

0 == 0 <=> True

#### and-or

在一个bool and a or b语句中，当bool条件为真时，结果是a；当bool条件为假时，结果是b。

有了它，原本需要一个if-else语句表述的逻辑：

`if a > 0:
    print ("big")
else:
    print ("small")`

就可以直接写成：

`print ((a > 0) and "big" or "small")`

**注意:**这里的and or语句是利用了python中的逻辑运算实现的，a本身不能是假值（如0，""）

***and-or真正的技巧在于，确保a的值不会为假。最常用的方式是使 a 成为 [a] 、 b 成为 [b]，然后使用返回值列表的第一个元素：***

`a = ""
b = "hell"
c = (True and [a] or [b])[0]
print (c)`

*由于[a]是一个非空列表，所以它决不会为假。即使a是0或者''或者其它假值，列表[a]也为真，因为它有一个元素。*

 

### 换行

如for循环中：       

`for i in range(0,5):`

​       ` print(*，end=''）#使print之后不换行`

`print() #换行`



### eval()

去掉参数最外层的引号

`eval(input())`*输入的内容不会被自动转化为字符串*



### 类型转换

`print(a, type(a))#显示a和a的数据类型（整数 浮点 bool 字符串）`

`int(x)     #把x转换成整数
float(x)  #把x转换成浮点数
str(x)     #把x转换成字符串
bool(x)   #把x转换成bool值`

**bool类型转换**：     

在python中，其他类型转成 bool 类型时，以下数值会被认为是False：

-**为0的数字**，包括0，0.0
-**空字符串**，包括''，""，一个空格不算空字符串
-表示空值的**None**
-**空集合**，包括()，[]，{}
其他的值都认为是True。

***在 if、while 等条件判断语句里，判断条件会自动进行一次bool的转换：***

`if a:`等于`if bool(a) == True:`或者`if a != ' '`   *a是一个字符串*



### 循环

#### break

强行跳出循环

`for i in range(10):
   a = input()
   if a == 'EOF':
       break`

#### continue

略过本次循环的余下内容，直接进入下一次循环

`if point < 60:
       continue`



### 列表list

#### 索引index

定义列表：`l = [365, 'xxx', 0.333, True]`

列表中每个元素对应一个递增的序号，从**0**开始

访问：`print(l[1])`  输出xxx

修改：直接赋值`l[0] = 111`

添加元素：`l.append(222)`列表变为[111, 'xxx', 0.333, Ture, 222]

删除元素：`del l[0]`

获取list元素个数：`count = len(l)`

负数索引：[-1]最后一个元素  [-3]倒数第三个元素

#### 切片slice

`print (l[1:3])`得到['xxx', 0.333]

开始位置包含在切片中，而结束位置不包括。

如果不指定第一个数，切片就从列表第一个元素开始。

如果不指定第二个数，就一直到最后一个元素结束。

都不指定，则返回整个列表。

切片中数字也可以使用负数。

#### 查找元素索引

`listname.index(item, start, end)`

*item待查找元素*  *start（可选）开始搜索的索引*   *end（可选）结束搜索的索引*



### 字符串

#### 格式化

**字符串可相加** `print(str1 + str2)` 或`print('very' + str)`

**字符串加数字**`print('xxx' + str(10) )`或`num = 10   print('xxx' + str(num))`或`print('xxx %d' % num)`   

***%d***整数 ***%f***小数 ***%.2f***保留两位小数 ***%s***字符串     

`name=''`

`score=233`

`print("%s xxxxx %d" % (name, score))`或`print("%s xxxxx %d" % ("xx", 123))`

#### 字符串分割

`字符串变量名.split()`

split默认按照空白字符进行分割。如**空格**，换行符**\n**，制表符**\f**。分割后的每一段都是一个新的字符串，最终返回这些字符串组成一个list。

split()还可以在括号中指定分割的符号。

例：1.`sentence = 'I am an English sentence'`

`sentence.split()`

`['I', 'am', 'an', 'English', 'sentence']`*#原来字符串中空格不再存在*

2.``section = 'Hi. I am the one. Bye.'``

`section.split('.')`

`['Hi', ' I am the one', ' Bye', '']`*#注意最后那个空字符串。每个'.'都会被作为分割符，即使它的后面没有其他字符，也会有一个空串被分割出来。*

#### join

***1.把一个list中的所有字符串连接成一个字符串***   例：

`s = ';'
li = ['apple', 'pear', 'orange']
fruit = s.join(li)
print(fruit)`

或

`fruit = ';'.join(['apple', 'pear', 'orange'])`

`print(fruit)`

得到`'apple;pear;orange'`

用来连接的字符串可以是多个字符，也可以是一个空串

***2.用连接符把字符串中的每个字符重新连接成一个新字符串***

`word = 'helloworld'`

`newword = ','.join(word)`

#### 遍历

`word = 'helloworld'
for c in word:
    print(c)`

#### 索引与切片同list

*字符串**不能**通过索引访问去更改其中的字符*

**切片：**[::]

第一个数字：开始位置，默认0

第二个数字：截止位置，默认列表长度

第三个数字：步长，默认1，**为-1时逆序切取**

#### 判断字符串中是否有某个子串

1.in和not in

`'xxx' in 'xxxxxxxx'`结果True 或 False

2.contains

`'xxxxxxxxxx'.__contains__('xxx')`返回True或False

3.find

`p = 'xxxxx某个字符串'.find('xxx子串')`

又出现，返回位置。没有返回-1

4.index

返回指定字符串在该字符串中第一次出现的索引（没有会出现异常）

`'xxxxxx'.index('xx')`

#### 替换字符串

`str.replace(old, new[, max])`*#方括号内第三个参数指替换次数不超过max次*

`str1 = 'xxxxxx'`

`str2 = str1.replace('要替换的', '替换成')`

或

`str1 = 'xxxxxxx'`

`str2 = str.replace(str1, '要替换的', '替换成')` 

#### 倒序输出

1.切片

`a = 'Helloworld'`

`print(a[::-1])`

2.reversed

`print(''.join(reversed(a)))`*reversed将字符串反转但结果不是字符串*



### 函数

例：`def sayHello():`    *def*:定义(define)一个函数   *sayHello*:函数的名字  *括号内为参数*

`return xxx`*函数返回值*

`def hello(name):
   print ('hello ' + name)`

`hello('world')`


程序就会输出

hello world

#### 默认参数

`def hello(name = 'world'):
   print ('hello ' + name)`


如果提供参数值时，这个参数就会使用默认值；如果提供了，就用提供的。

这样，在默认情况下，你只要调用

`hello()`

就可以输出hello world

*#当函数有多个参数时，如果想给部分参数提供默认参数，那么这些参数必须在参数的末尾。*



### 模块

#### 调用模块

`import random`

`random.randint(1, 10)
random.choice([1, 3, 5])`

*函数前面需要加上“random.”，这样python才知道要调用random中的方法。*

只是用到random中的某一个函数或变量，也可以通过from...import...指明：

`from math import pi as math_pi #as...给引入的方法换个名字
print (math_pi)`

random中有哪些函数和变量？

`dir(random)`

#### 数学运算模块math

`import math`

两个常量：

`math.pi # 圆周率π：3.141592...
math.e # 自然常数：2.718281...`


数值运算：

`math.ceil(x)`  `#对x向上取整，比如x=1.2，返回2.0（py3返回2）`

`math.floor(x)`  `#对x向下取整，比如x=1.2，返回1.0（py3返回1）`

`math.pow(x,y)`   `#指数运算，得到x的y次方`

`math.log(x)`   `#对数，默认基底为e。可以使用第二个参数，来改变对数的基底。比如math.log(100, 10)`

`math.sqrt(x)`   `#平方根`

`math.fabs(x)`   `#绝对值`


三角函数: 

`math.sin(x)
math.cos(x)
math.tan(x)
math.asin(x)
math.acos(x)
math.atan(x)`
*注意：这里的x是以弧度为单位，所以计算角度的话，需要先换算*

角度和弧度互换: 

`math.degrees(x)`   `#弧度转角度`

`math.radians(x)`   `#角度转弧度`



### 字典

***在字典中，名字叫做“键”，对应的内容信息叫做“值”。字典是一个键/值对的集合。***

`d = {'key1': 'value1', 'key2': 'value2'}`

键/值对用冒号分割，每个对之间用逗号分割，整个字典包括在花括号中。

**注意**：

1.键必须是唯一的；

2.键只能是简单对象，比如字符串、整数、浮点数、bool值。

​    *list就不能作为键，但是可以作为值。*

#### 访问字典中元素

`print(d['key1'])`或`d.get('key1')`

*如果键是字符串，通过键访问时需要加引号*

#### 通过for...in遍历

`for key in d:`

​         `    print(d[key])`

*遍历的变量中存储的是字典的键。*

#### 改变值

1.改变某一项的值，直接给这一项赋值：

`d['key1'] = 'value1.1'`

2.增加一项字典项的方法是，给一个新键赋值：

`d['key3'] = 'value3'`

3.删除一项字典项的方法是del：

`del d['key2']`
*注意，这个键必须已存在于字典中*

4.如果新建一个空的字典，只需要:

`d = {}`









 



















