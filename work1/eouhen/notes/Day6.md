## 列表
### 创建
- ==lst1 = \['string',123,'hello']==
- ==lst2 = list(\['string',123,'hello'])==
- 列表对象中存储该列表的id值，该列表的值是里面存储对象的id值，存储对象的id值分别指向各自的内存空间
### 特点
- 有序可变
- 列表元素按顺序有序排序
- 索引映射唯一的数据
左→右：从0开始递增；右←左：从-1开始递减
- 列表可以存储重复数据
- 任意数据类型混存
- 根据需要动态分配和回收内存
### 查询
#### 获取列表中指定元素的索引：==list.index()==
- 如列表中存在n个相同元素，只返回相同元素中的第一个元素的索引
- 如果查询的元素在列表中不存在，报错ValueError
- 还可以在指定的start和stop之间进行查找，包括start但不包括stop：==list.index(元素,start,stop)==
#### 获取列表中的单个元素
- 正向索引：从0到N-1
- 逆向索引：从-N到-1
- 指定索引不存在时，报错IndexError
#### 获取列表中的多个元素（切片）：==list\[start : stop : step]==
- 切片结果：原列表片段的拷贝
- 切片范围：\[start,stop) 无论正向逆向stop都不包括！
- 省略step时，step值默认为1
- step为正数，从start开始往后计算切片，\[ : stop : step]：默认从第一个开始，\[start : : strp]：默认到最后一个结束
- step为负数，从start开始往前计算切片，\[ : stop : step]：默认从最后一个开始，\[start : : strp]：默认到第一个结束
#### 判断指定元素在列表中是否存在
- in
- not in
### 遍历
**==for 自定义变量 in 列表名 : 
	循环体==**

### 增删改
#### 增
- ==list.append(x)==：向列表末尾添加一个元素
- ==list.extend(x)==：向列表末尾至少添加一个元素
```python
list1 = [1,2,3,4]  
list2 = ['hello','world']  
list1.append(list2)  
print(list1) 
# [1, 2, 3, 4, ['hello', 'world']] 
# 将list2作为一个元素添加到list1末尾
list1.extend(list2)  
print(list1) 
# [1, 2, 3, 4, ['hello', 'world'], 'hello', 'world']
# 将list2的所有元素分别添加到list1末尾
```
- ==list.insert(index , x)==：向列表任意位置添加一个元素
- 切掉替换：向列表任意位置至少添加一个元素
```python
list1 = [1,2,3,4]
list2 = ['hello','world']
list1[2:] = list2
# [1, 2, 'hello', 'world']
# 将list1从index=2到结尾的元素替换成list2里的元素
```
#### 删
- ==list.remove(x)==：一次删除一个元素，重复元素只删除第一个，元素不存在时报错ValueError
- ==list.pop(index)==：删除一个指定索引位置上的元素，指定索引不存在时报错IndexError，不指定索引，删除列表中最后一个元素
- 切掉替换：使用空列表替换列表的指定切片
```python
list1 = [1,2,3,4]  
list1[1:3] = []  
print(list1)
# [1, 4]
```
- ==list.clear()==：清空列表元素
- ==del==：删除列表对象
#### 改
- 为指定索引的元素赋予一个新值
- 为指定的切片赋予一个新值

### 排序
- 调用==list.sort()==
列表中的所有元素默认按照从小到大的升序顺序进行排序，可指定==list.sort(reverse=True)==进行降序，没有产生新列表
- 调用内置函数sorted()
可指定==sorted(list,reverse=True)==进行降序，产生新列表，原列表不发生改变
```python
list1 = [25,10,5,60,45]  
new_list = sorted(list1)  
print(list1)     # [25, 10, 5, 60, 45]
print(new_list)  # [5, 10, 25, 45, 60]
desc_list = sorted(list1,reverse=True)  
print(desc_list) # [60, 45, 25, 10, 5]
```
### 列表生成式
==list = \[ expression for i in range(x) ]==
expression表示列表元素的表达式，通常包含自定义变量i