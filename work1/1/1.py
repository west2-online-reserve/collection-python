import re
x,y,z=re.split("[ ,.，、|\/]",input("3,2,1："))
x,y,z=int(x),int(y),int(z)
minNum=max(x,y,z)
maxNum=min(x,y,z)
print(minNum,x+y+z-minNum-maxNum,maxNum)




