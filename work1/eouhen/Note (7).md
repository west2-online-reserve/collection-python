## 字典

### 创建
- ==dict1 = \{键1:值1 , 键2:值2 , ...}==
- ==dict2 = dict(键1=值1 , 键2=值2 , ...)==
### 特点
- 无序可变
- 字典中的元素是无序的
- key必须是不可变对象，不允许重复（否则覆盖）
- 可根据需要动态伸缩
- 每个键值对的存储位置通过哈希函数（hash）计算得出
- 查找速度快，浪费内存较大
### 查询
#### 获取字典中的元素
- ==dict1\['keyname']==
若字典中不存在指定的key，则报错KeyError
- ==dict1.get('keyname')==
若字典中不存在指定的key，不报错，返回None，可以通过参数设置默认的value
```python
print(dict1.get('不存在的键名',0)) 
# 打印0
```
#### 获取字典视图
- ==dict1.keys()==：获取字典中的所有keys
- ==dict1.values()==：获取字典中的所有values
- ==dict1.items()==：获取字典中的所有key-value对，得到元组
#### 判断指定key在字典中是否存在
- in
- not in

### 遍历
**==for i in 字典名 : 
	print(i , 字典名[i] , 字典名.get(i))==**
注：i打印键名，字典名\[i]或字典名.get(i)打印值
### 增删改
#### 删
- 删除指定的键值对：==del dict1\['keyname']==
- 清空字典元素：==dict1.clear()==
#### 增
- 新增键值对：==dict1\['newKeyname'] = newValue==
#### 改
- 修改键值对：==dict1\['指定Keyname'] = newValue==

### 字典生成式
- 内置函数==zip()==：用于将可迭代的对象作为参数，将对象中对应的元素打包成一个元组，然后返回由这些元组组成的列表
```python
items = ['Frults','Books','Others']
prices = [96,78,85]
d = {i.upper():j for i,j in zip(items,prices)}
print(d)
# {'FRULTS': 96, 'BOOKS': 78, 'OTHERS': 85}
```