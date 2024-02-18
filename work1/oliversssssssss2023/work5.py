student_dict = {}

student_dict[101] = '小明'
student_dict[102] = '小红'
student_dict[103] = '小刚'
student_dict[104] = '小雨'
student_dict[105] = '小夏'

keyremove = []
for key in student_dict.keys():
    if key % 2 == 0:
        keyremove.append(key)

for key in keyremove:
    del student_dict[key]

print(student_dict)