# 法一：直接上手在原处修改代码（fail！）
# def listt(list):
#     n=len(list)
#     for i in range(n):
#         if type(list[i])==str :
#             if i!=n-1:
#                 list=list[:i]+list[i+1:]
#             else:6
#                 list=list[:i]
#     return list
# print(listt([454,"4542454",44563,"hsghdf"]))
# 失败版本！在迭代时修改了列表的长度，可能会导致循环索引混乱！

# 法二：新建一个列表尝试（直接list.sort(reverse=False)）[True为降！]
# def listt(list):
#     n=len(list)
#     list2=[]
#     for i in range(n):
#         if type(list[i])!=str:
#             list2.append(list[i])
#     list2.sort(reverse=False)
#     return list2
# print(listt([454,"4542454",44563,"hsghdf"]))


# 补充：要对一个包含整数的列表进行排序，你可以使用Python的内置函数 sorted() 或者列表的方法 sort()。这两种方法都可以实现对整数列表的升序排序。
# 下面是使用这两种方法进行整数列表排序的示例代码：
# 使用 sorted() 函数：
# python
# Copy code
# integer_list = [10, 5, 8, 3, 7, 1]
# 
# sorted_list = sorted(integer_list)  # 使用 sorted() 函数进行排序，不改变原列表
# print(sorted_list)
# 使用 sort() 方法：
# 
# python
# Copy code
# integer_list = [10, 5, 8, 3, 7, 1]
# 
# integer_list.sort()  # 使用 sort() 方法对原列表进行排序，不返回新列表
# print(integer_list)
# 无论你选择使用哪种方法，都会得到一个升序排列的整数列表。如果你需要降序排序，可以在调用这些函数时传递 reverse=True 参数。
# 
# 例如，使用 sorted() 函数进行降序排序：
# 
# python
# Copy code
# integer_list = [10, 5, 8, 3, 7, 1]
# 
# sorted_list_descending = sorted(integer_list, reverse=True)
# print(sorted_list_descending)
# 使用 sort() 方法进行降序排序：
# 
# python
# Copy code
# integer_list = [10, 5, 8, 3, 7, 1]
# 
# integer_list.sort(reverse=True)
# print(integer_list)
# 这些代码示例中的输出都将是排序后的列表，根据你选择的排序方式（升序或降序）。
# 法三：利用sortlist=sorted(list,reverse=False)
# def listt(list):
#     n=len(list)
#     list2=[]
#     for i in range(n):
#         if type(list[i])!=str:
#             list2.append(list[i])
#     list2=sorted(list2,reverse=False)
#     return list2
# print(listt([454,"4542454",44563,"hsghdf"]))




