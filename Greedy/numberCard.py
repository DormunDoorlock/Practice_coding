from xml.dom import minicompat


n,m = map(int, input().split())
result =0

for i in range(n):
    data = list(map(int, input().split()))
    data.sort()
    min = data[0]
    if result < min :
        result=min

print(result)