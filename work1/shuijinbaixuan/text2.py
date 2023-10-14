x=int (input())
y=int (input())
z=int (input())
if x>y:
    if z<y:
        print('%d %d %d' %(x,y,z))
    elif x>z:
        print('%d %d %d' %(x,z,y))
    else:
        print('%d %d %d' %(z,x,y))
else:
    if z<x:
        print('%d %d %d' %(y,x,z))
    elif y>z:
        print('%d %d %d' %(y,z,x))
    else:
        print('%d %d %d' %(z,y,x))
