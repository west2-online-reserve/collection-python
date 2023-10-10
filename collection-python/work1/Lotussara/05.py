dict={101:"甲",102:"乙",103:"丙",104:"丁"}
for num in list(dict):
    if num%2==0:
        del dict[num]
print(dict)

