n= input()
plans=input().split()
x=1
y=1

for i in plans:
    if i=='L':
      if y!=1:
        y-=1

    if i=='R':
      if y!=5:
        y+=1

    if i=='U':
      if x!=1:
        x-=1

    if i=='D':
      if x!=5:
        x+=1

print(x,y)


