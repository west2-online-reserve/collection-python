## 输出函数print()
#### 将数据输出到文件中
注：所指定的盘符需存在，同时使用file = fp
a+表示如果文件不存在就创建，存在就在文件内容的后面继续追加
```python
fp = open('E:/text.txt','a+')  
print('helloworld',file = fp)  
fp.close()
```
#### 不进行换行输出
```python
print('hello','word','Python')
```

## 转义字符与原字符
#### 转义字符
反斜杠+想要实现的转义功能的首字母，如
反斜杠：\\\\
单引号：\\'
双引号：\\"
换行newline：\\n
回车return（光标移动到本行的开头）：\\r
制表符tab（/t为4个制表位）：\\t
退格backspace（向左删除一个字符）：\\b

#### 原字符
不希望字符串中的转义字符起作用，就使用原字符，就是在字符串之前加上r或R
```python
print(r'hello\nworld')
print('hello\\nworld')
```
注：最后一个字符不能是反斜杠，但可以是连着两个反斜杠
```python
print(r'hello\nworld\')
	  # 这是错的
```