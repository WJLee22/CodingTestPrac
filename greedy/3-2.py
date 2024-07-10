n,m,k = map(int, input('n,m,k 입력=>').split())
data=list(map(int,input('숫자들 입력=>').split()))

data.sort()

first=data[n-1]
second=data[n-2]

result=0

count=int(m/(k+1))*k
count+=m%(k+1)

result+=(count) * first
result+=(m-count)*second
 
print(result)

