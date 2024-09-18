data=input()

column=int(ord(data[0]))-int(ord('a'))+1
row=int(data[1])


move=[(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]

sum=0

for i in move:

    move_row= row+i[0]
    move_column=column+i[1]

    if  move_row>=1 & move_row<=8 & move_column>=1 & move_column<=8 :
        sum+=1

print(sum)
