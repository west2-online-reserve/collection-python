#输入⼀个列表（list），列表中含有字符串和整数，删除其中的字符串元素，然后把剩下的整数升序排序，输出列表
ls =[1,2,4,'eef',34,'rtgr','34']
ls2 = [i for i in ls if isinstance(i, int)]
ls2.sort(reverse=False)
print(ls2)