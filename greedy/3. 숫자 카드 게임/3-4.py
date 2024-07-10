m,n= map(int,input("행(m) 열(n) 입력=>").split())

biggest=0

for _ in range(n):
  data=list(map(int,input().split()))

  min_value=10001

  for i in data:
    min_value=min(min_value,i)

  biggest=max(min_value,biggest)

print(biggest)