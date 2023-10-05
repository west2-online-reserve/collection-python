# 1-基础语法

- 配环境
- 推荐教程
- 初学者作业
- 有基础者作业
- 作业要求
- 有想学人工智能学习的同学注意
- 预习下⼀轮
- 考核截止日期
- 提交方式

## 配环境

下载pycharm [PyCharm：JetBrains为专业开发者提供的Python IDE](https://www.jetbrains.com.cn/pycharm/)

一开始学下载社区版

想要用专业版可以申请学生免费许可证

想搞人工智能的电脑最好有好点的显卡，实在没有只能搞gpu云服务了

想搞人工智能的去装个anaconda

## 推荐教程

1. Crossin编程教室 [Python 入门指南 (python666.cn)](https://python666.cn/cls/lesson/list/)

2. Python - 100天从新手到大师的前10节课 [jackfrued/Python-100-Days: Python - 100天从新手到大师 (github.com)](https://github.com/jackfrued/Python-100-Days)

3. Python官方文档 [3.10.7 Documentation (python.org)](https://docs.python.org/zh-cn/3/)

4. 菜鸟教程 [Python3 教程 | 菜鸟教程 (runoob.com)](https://www.runoob.com/python3/python3-tutorial.html)

5. 廖雪峰的官⽅教程 [Python教程 - 廖雪峰的官方网站 (liaoxuefeng.com)](https://www.liaoxuefeng.com/wiki/1016959663602400)

6. b站能学的视频太多了，但是大部分时间太长，难以坚持看下去，可以先对着上面的教程看，有看不懂的再去找对应的视频

7. 关于Python的学习路线和一些常见问题 [code-roadmap/Python学习路线.md at main · liyupi/code-roadmap (github.com)](https://github.com/liyupi/code-roadmap/blob/main/docs/roadmap/Python学习路线.md)


## 初学者作业

1. 输入三个整数x,y,z，请尝试用多种方式把这三个数由大到小输出
2. 输出九九乘法表
3. 输入⼀个字符串，判断字符串中是否含有"ol"这个⼦串，若有把所有的"ol"替换为"fzu"，最后把字符串倒序输出
4. 输入⼀个列表（list），列表中含有字符串和整数，删除其中的字符串元素，然后把剩下的整数升序排序，输出列表
5. 创建一个字典（dict），为字典添加几个键为学号，值为姓名元素，删除学号尾号为偶数的元素，输出字典
6. 创建一个函数，这个函数可以统计一个只有数字的列表中各个数字出现的次数，通过字典方式返回
7. 设计⼀个商品类，它具有的私有数据成员是商品序号、商品名、单价、总数量和剩余数量。具有的 公有成员函数是：初始化商品信息的构造函数__init__，显示商品信息的函数display，计算已售出 商品价值income，修改商品信息的函数setdata
8. （可选）尝试用所学的知识写一个斗地主随机发牌程序，将每个人的发牌以及多的三张牌的结果分别输出到player1.txt，player2.txt，player3.txt，others.txt四个文件中，可以不要求牌的花色

## 有基础者作业

1. 实现一个装饰器，在开始执行函数时输出该函数名称， 并在结束时输出函数的开始时间和结束时间以及运行时间

2. 用所学的知识写一个斗地主随机发牌程序，将每个人的发牌以及多的三张牌的结果分别按照从大到小的顺序输出到player1.txt，player2.txt，player3.txt，others.txt四个文件中

3. 写一个列表推导式，生成一个5*10的矩阵，矩阵内的所有值为1，再写一个列表推导式，把这个矩阵转置

4. 了解类的魔术方法(Magic Method)。创建类MyZoo，实现以下功能：

    - 具有字典anmials，动物名称作为key，动物数量作为value

    - 实例化对象的时候，输出"My Zoo!" 

    - 创建对象的时候可以输入字典进行初始化,若无字典传入，则初始化anmials为空字典

        ```python
        myzoooo = MyZoo({"pig":5,'dog':6}) 
        myzoooo = MyZoo() 
        ```

        

    -  print(myzoooo) 输出 动物名称和数量

    - 比较两个对象是否相等时，只要动物种类一样，就判断相等： 

        ```python
        输入：
        myzoooo1 = MyZoo({'pig':1})
        myzoooo2 = MyZoo({'pig':5})
        print(myzoooo1 == myzoooo2)
        输出:
        My Zoo!
        My Zoo!
        True
        ```

        

    - len(myzoooo) 输出所有动物总数

5. （可选）写一个正则表达式，用于验证用户密码，长度在6~18 之间，只能包含英文和数字

## 作业要求

1. 不要抄袭哦
2. 遇到不会的时候先自己去网上找资料，实在找不到在来问，用搜索引擎解决问题的能力非常重要
3. 例如输入输出的格式可以自己决定，但是要符合题目要求
4. 有基础者的只需要做有基础者作业即可

## 有想学人工智能学习的同学注意

我们会在第二轮考核结束后进行一次面试，进行人工智能方向和后端方向的分流。

对人工智能感兴趣的同学可以提前做好以下准备：

1. 机器学习理论知识：推荐教程：吴恩达机器学习 https://study.163.com/course/introduction/1210076550.htm （当然其他教程也可）打好基础很重要。
2. Python的numpy和pandas库的使用：便于数据处理，数据处理也很重要捏。

## 预习下⼀轮

1. 爬虫是什么？
2. 了解正则表达式
3. 了解requests，selenium等库，有能力的可以尝试学习scrapy框架
4. 了解lxml或者BeautifulSoup
5. 了解mysql数据库的使用方法
6. 注册GitHub账号，学习git的使用
7. 了解基础的网页架构（html+css）
8. 爬虫教程 https://cuiqingcai.com/5052.html +b站视频也很多