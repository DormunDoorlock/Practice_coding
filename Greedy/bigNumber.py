import sys


n,m,k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first=data[-1]
second=data[-2]

result=0

cnt= m // (k+1)
rest = m % (k+1)

add = first * k + second
result = add * cnt + first * rest

print(result)