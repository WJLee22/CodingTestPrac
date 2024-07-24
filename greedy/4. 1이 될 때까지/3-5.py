n, k = map(int, input('n,k 입력=>').split())

count = 0

while True:

  if n == 1:
    break

  count += 1

  if n % k == 0:
    n /= k
  else:
    n -= 1

print(count)
