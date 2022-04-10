def check(glass,size):
    ng= len(glass)
    for i in range(ng):
        for j in range(ng):
            if glass[i][j]<size and glass[i][j]!=0:
                return True
    return False

def fishCount(n,glass,size,rest):
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    mp=[]
    for i in range(n):
        for j in range(n):
            if glass[i][j]==9:
                xf=i
                yf=j
    b=[]
    b.append(xf)
    b.append(yf)
    mp.append(b)
    cnt=0
    print(mp,size,rest)
    x=2
    while True:
        print(glass)
        cnt +=1
        mpp=[]
        for j in range(len(mp)):
            mpp.append(mp[j])
        for i in range(len(mp)):
            for j in range(4):
                mxf=mp[i][0]+dx[j]
                myf=mp[i][1]+dy[j]
                if mxf>=n or myf >=n or mxf<0 or myf<0:
                    continue
                if glass[mxf][myf]>size:
                    continue
                a=[]
                a.append(mxf)
                a.append(myf)
                mp.append(a)
        for k in range(len(mpp)):
            mp.remove(mpp[k])
        result = []    
        for value in mp:
            if value not in result:
                result.append(value)
        mp=result
        print(mp)

        for mPoint in mp:
            if glass[mPoint[0]][mPoint[1]] !=0 and glass[mPoint[0]][mPoint[1]]<size :
                rest -=1
                if rest ==0:
                    size +=1
                    rest=size
                for i in range(n):
                    for j in range(n):
                        if glass[i][j]==9:
                            glass[i][j]=0
                glass[mPoint[0]][mPoint[1]]=9
                return cnt,size,rest
            else:
                continue
# 최단거리 생각 못함 => BFS 사용할 것
# BFS DFS 다시 생각해볼것 && 단순 구현인지 파악할것 

n= int(input())
glass = []
for i in range(n):
    glass.append(list(map(int,input().split())))
size = 2
rest = size
cnt=0
xx=2
while True:
    if check(glass,size) != True:
       print(cnt)
       break
    
    ccnt,size,rest= fishCount(n,glass,size,rest)
    print(ccnt)
    cnt += ccnt

    

