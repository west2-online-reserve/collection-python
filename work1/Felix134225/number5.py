student={}
student[123]='小张'
student[124]='小李'
student[125]='小陈'
student[126]='小林'
student[127]='小王'
student[128]='小周'
student[129]='小戴'
student[130]='小杨'
delect=[]
for key in student:
    if key%2==0:
        delect.append(key)
for key in delect:
    del student[key]
print(student)