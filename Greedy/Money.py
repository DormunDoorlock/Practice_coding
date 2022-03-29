money = int(input())
cnt=0

money_list=[500,100,50,10]

for i in money_list:
    cnt += money // i
    money= money % i

print(cnt)