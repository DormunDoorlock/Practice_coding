def cal_eaning(order,data,out):
    out_count=0
    re=0
    start=out
    ground=[0,0,0]
    ct=0
    while True:
        hit=data[order[start]]
        # out 된 경우 , out 카운트 +1 , out 카운트 3 인경우 이닝 종료
        if hit == 0:
            out_count += 1
            if out_count ==3:
                if start==8:
                    return re,0
                else:
                    return re,start+1
        # 홈런인 경우, 1루,2루,3루 그라운드 인원수 +1 점수 획득, ground 초기화 
        if hit == 4:
            cnt=0
            for player in ground:
                if player != 0:
                    cnt +=1
            cnt +=1
            re += cnt
            ground =[0,0,0]
        # 3루타인 경우, 1루,2루,3루 그라운드 인원수 점수 획득, player 3루
        if hit ==3:
            cnt=0
            for player in ground:
                if player != 0:
                    cnt +=1
            re += cnt
            ground =[0,0,1]
        # 2루타인 경우, 2루 3루 그라운드 인원수 점수 획득, 1루 -> 3루 , player 2루
        if hit ==2:
            cnt=0
            for i in reversed(range(3)):
                if ground[i]==1:
                    if i==1 or i==2:
                        cnt +=1
                        ground[i]=0
                    else:
                        ground[2]=1
                        ground[i]=0
                else:
                    continue
            ground[1]=1
            re += cnt
        # 1루타인 경우, 3루 그라운드 인원수 점수 획득, 1루 -> 2루 , 2루 -> 3루, player 1루
        if hit ==1:
            cnt=0
            for i in reversed(range(3)):
                if ground[i]==1:
                    if i==2:
                        cnt +=1
                        ground[i]=0
                    elif i==1:
                        ground[2]=1
                        ground[i]=0
                    else:
                        ground[1]=1
                        ground[i]=0
                else:
                    continue
            ground[0]=1
            re += cnt      
        # 모든 타순이 끝난 경우, 다음 타선으로 연결
        if start==8:
            start=0
        else:
            start +=1
            
def cal(arr,data):
    arr.insert(3,0)
    out_position=0
    a_result=0
    #print(arr)
    inning=0
    while True:
        if inning == len(data):
            return a_result
        out=0
        b1,b2,b3=0,0,0
        while True:
            if out==3:
                break
            hit=data[inning][arr[out_position]]
            if hit==0:
                out+=1
            if hit==4:
                a_result += b1+b2+b3+1
                b1,b2,b3=0,0,0
            if hit==3:
                a_result += b1+b2+b3
                b1,b2=0,0
                b3=1
            if hit==2:
                a_result += b2+b3
                b3=b1
                b1=0
                b2=1
            if hit==1:
                a_result +=b3
                b3=b2
                b2=b1
                b1=1
            if out_position==8:
                out_position=0
            else:
                out_position +=1
            
        inning +=1   
    arr.remove(0)
    return a_result
'''
def per(arr,data):
    used=[0 for _ in range(8)]
    mx=[]
    def generate(chosen,used,mx):
        if len(chosen)==8:
            result=cal(chosen,data)
            mx.append(result)
            return 
        
        for i in range(8):
            if not used [i]:
                chosen.append(arr[i])
                used[i]=1
                generate(chosen,used,mx)
                print(chosen)
                used[i]=0
                chosen.pop()
    generate([],used,mx)
    return max(mx)
 '''   
n = int(input())

data=[]
for i in range(n):
    e=list(map(int,input().split()))
    data.append(e)

ans=0
import itertools
cases = list(itertools.permutations([1,2,3,4,5,6,7,8], 8)) 
for case in cases:
    #print(case)
    ans = max(ans, cal(list(case),data))
print(ans)
    
    