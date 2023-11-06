## range()函数
用于生成一个整数序列，返回值是一个迭代器对象
- **==range(stop)==** 创建一个\[0,stop)之间的整数序列，步长默认为1
- **==range(start,stop)==** 创建一个\[start,stop)之间的整数序列，步长默认为1
- **==range(start,stop,step)==** 创建一个\[start,stop)之间的整数序列，步长为step
- 特点：不管range对象表示的整数序列有多长，所有range对象占用的内存空间都是相同的，因为仅仅需要存储start、stop和step。只有当用到range对象时，才会去计算序列中的相关元素。
## 循坏结构
### while
**==while 条件表达式:
	条件执行体（循坏体）==**
### for-in
**==for 自定义变量 in 可迭代对象:
	循环体==**
```python
for i in 'Python': #第一次取出来的值是'P'，将'P'赋值给i，并将i的值输出
	print(i)
# P y t h o n (打印在不同的行上)
for i in range(10):
	print(i)
# 0 1 2 3 4 5 6 7 8 9
for _ in range(5):
	print('与_无关的内容')
# 如果在循环体中不需要使用到自定义变量，可将自定义变量写为“_”
```
## 流程控制语句
- break
结束整个循环，进入循环后的代码块
- continue
结束当前循环，进入下一次循环
```python
# 使用continue打印1-50中所有5的倍数
for i in range(1,51):
	if i%5!=0:
		continue
	print(i)
```
## else语句
- ==if ... :
	...
else :
	...==
if条件表达式不成立时执行else
- ==while ... :
	...
else :
	...==
- ==for ... :
	...
else :
	...==
没有碰到break时执行else
## 嵌套循环
九九乘法表
```python
for i in range(1,10):  
    for j in range(1,i+1):  
        print(str(i)+'*'+str(j)+'='+str(i*j),end='\t')  
    print()
```
注：end=''，将引号之间的内容作为字符串传递给print()函数字符串的末尾，代替默认的换行符