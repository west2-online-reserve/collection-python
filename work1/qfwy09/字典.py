#字典
student_dict = {}
student_dict["202101"] = "张三"
student_dict["202102"] = "李四"
student_dict["202103"] = "王五"
student_dict["202104"] = "赵六"
student_dict["202105"] = "孙七"
print("原字典：", student_dict)
for key, value in list(student_dict.items()):
    if int(key[-1]) % 2 == 0:
        del student_dict[key]
print("删除偶数尾号后的字典：", student_dict)
