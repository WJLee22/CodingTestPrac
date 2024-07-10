m,n= map(int,input("행(m) 열(n) 입력=>").split())

biggest=0

for _ in range(n):
  data=list(map(int,input().split()))

  biggest=max(biggest,min(data))

print(biggest)