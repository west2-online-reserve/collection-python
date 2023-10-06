x=int (input())
y=int (input())
z=int (input())
if x>y:
      if z>x:
            print('%d %d %d' %(z,x,y))
      elif z<y:
            print('%d %d %d' %(x,y,z))
      else:
            print('%d $d %d' %(x,z,y))
else:
      if z<x:
            print('%d %d %d' %(y,x,z))
      elif z>y:
            print('%d %d %d' %(z,y,x))
      else:
            print('%d %d %d' %(y,z,x))
