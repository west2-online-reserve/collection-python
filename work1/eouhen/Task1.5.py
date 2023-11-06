# Author : AnnieHathaway
stu_id = [i for i in range(1, 9)]
stu_name = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh']
stu_dict = {i: j for i, j in zip(stu_id, stu_name)}
for i in stu_dict:
    print(stu_dict[i])
'''for i in stu_dict:
    if int(stu_dict[i])%2==0 :
        del stu_dict[i]
print(stu_dict)'''
# 删除学号尾号为偶数的元素
keys_to_delete = []
for student_id in stu_dict.keys():
    if student_id % 2 == 0:
        keys_to_delete.append(student_id)

for key in keys_to_delete:
    del stu_dict[key]

print(stu_dict)