from collections import deque
N,Q=map(int,input().split())
l=1
for _ in range(N):
    l *=2
data =[]
for _ in range(l):
    data.append(list(map(int,input().split())))
order=list(map(int,input().split()))

dx=[-1,0,1,0]
dy=[0,1,0,-1]

for i in range(len(order)):
    rotate=[item[:] for item in data]
    if order[i] !=0:
        pl=1
        for _ in range(order[i]):
            pl *=2
        for x in range(0,l,pl):
            for y in range(0,l,pl):
                for a in range(pl):
                    for b in range(pl):
                        rotate[b+x][pl-1-a+y]=data[a+x][b+y]
        data=[item[:] for item in rotate]
    for x in range(l):
        for y in range(l):
            if data[x][y]==0:
                continue
            n=0
            for k in range(4):
                ax=x+dx[k]
                ay=y+dy[k]
                if ax<0 or ay<0 or ax>=l or ay >=l:
                    continue
                else:
                    if rotate[ax][ay] != 0:
                        n +=1
            if n <3 :
                data[x][y] -=1
result=0
m=0
def BFS(g,sx,sy,visit):
    rs=[]
    zx=[-1,0,1,0]
    zy=[0,1,0,-1]
    queue=deque()
    rs.append((sx,sy))
    queue.append((sx,sy))
    visit[sx][sy]=1
    while queue:
        v= queue.popleft()
        x=v[0]
        y=v[1]
        for i in range(4):
            rx=x+zx[i]
            ry=y+zy[i]
            if rx<0 or ry<0 or rx>=len(g) or ry>=len(g):
                continue
            if g[rx][ry] ==0 or visit[rx][ry] ==1:
                continue
            queue.append((rx,ry))
            rs.append((rx,ry))
            visit[rx][ry]=1
    return rs
    
visited=[[0]*l for _ in range(l)]
for x in range(l):
    for y in range(l):
        if data[x][y] !=0:
            result +=data[x][y]
            if visited[x][y] ==0:
                re=BFS(data,x,y,visited)
                if len(re)>m:
                    m=len(re)
                
print(result)
print(m)