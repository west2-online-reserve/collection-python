#创建一个字典（dict），为字典添加几个键为学号，值为姓名元素，删除学号尾号为偶数的元素，输出字典
dic={1000:'Amy',1001:'Tom',1003:'Jack',1004:'Abc'}
dic2={i:dic[i] for i in dic if i%2==1}
print(dic2)