N = int(input())

data=[]
for _ in range(N):
    data.append(list(map(int,input().split())))

start=int((N-1)/2)
visited=[[0]*N for _ in range(N)]
dx=[0,1,0,-1]
dy=[-1,0,1,0]
d=0
x=start
y=start
visited[x][y]=1
rx=[
    [-1,1,-2,2,-1,1,-1,1,0],
    [0,0,1,1,1,1,2,2,3],
    [-1,1,-2,2,-1,1,-1,1,0],
    [0,0,-1,-1,-1,-1,-2,-2,-3]
]
ry=[
    [0,0,-1,-1,-1,-1,-2,-2,-3],
    [-1,1,-2,2,-1,1,-1,1,0],
    [0,0,1,1,1,1,2,2,3],
    [-1,1,-2,2,-1,1,-1,1,0]
]
result =0
while True:
    #print(x,y)
    nd=(d+1)%4
    ax=x+dx[d]
    ay=y+dy[d]
    nx=ax+dx[nd]
    ny=ay+dy[nd]
    
    if data[ax][ay] !=0:
        dust=data[ax][ay]
        data[ax][ay]=0
        r_d=0
        for i in range(9):
            if i<2:
                m=int(dust*0.01)
            elif i<4:
                m=int(dust*0.02)
            elif i<6:
                m=int(dust*0.07)
            elif i<8:
                m=int(dust*0.1)
            else:
                m=int(dust*0.05)
            r_d +=m
            mx=x+rx[d][i]
            my=y+ry[d][i]
            if mx<0 or my<0 or mx>=N or my>=N:
                result +=m
            else:
                data[mx][my] += m
        alp=dust-r_d
        mx=x+2*dx[d]
        my=y+2*dy[d]
        if mx<0 or my<0 or mx>=N or my>=N:
            result += alp
        else:
            data[mx][my] += alp
            
    if x==0 and y ==0:
        break
    if visited[nx][ny]==1:
        visited[ax][ay]=1
        x=ax
        y=ay
    
    elif visited[ax][ay]==0:
        visited[ax][ay]=1
        x=ax
        y=ay
        d= (d+1)%4
print(result)