from collections import deque

N,M = map(int,input().split())

data=[]
score=0
for _ in range(N):
    data.append(list(map(int,input().split())))

    
def BFS(g,sx,sy,visited):
    result=[]
    queue=deque()
    queue.append((sx,sy))
    result.append((sx,sy))
    visited[sx][sy]=1
    color=g[sx][sy]
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    while queue:
        v=queue.popleft()
        for i in range(4):
            x=v[0]+dx[i]
            y=v[1]+dy[i]
            if x<0 or x>=len(g) or y<0 or y>=len(g):
                continue
            if visited[x][y]==0:
                if g[x][y]==color or g[x][y]==0:
                    result.append((x,y))
                    queue.append((x,y))
                    visited[x][y]=1
    #print(visited)
    return result               
while True:                
    rx=0
    ry=0
    r=[]
    visited=[[0]*N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if visited[x][y]==0 and data[x][y]!=-1 and data[x][y]!=0 and data[x][y]!=-2:
                visit=visited[:]
                re=BFS(data,x,y,visit)
                for (a,b) in re:
                    if data[a][b]==0:
                        visit[a][b]=0
                if len(re)>len(r):
                    rx=x
                    ry=y
                    r=re[:]
                elif len(re)==len(r):
                    re_len=0
                    r_len=0
                    for i in range(len(re)):
                        if data[re[i][0]][re[i][1]]==0:
                            re_len+=1
                    for i in range(len(r)):
                        if data[r[i][0]][r[i][1]]==0:
                            r_len+=1
                    if re_len>r_len:
                        rx=x
                        ry=y
                        r=re[:]
                    elif re_len==r_len:
                        if x>rx:
                            rx=x
                            ry=y
                            r=re[:]
                        elif x==rx:
                            if y>ry:
                                rx=x
                                ry=y
                                r=re[:]
    if len(r)<2:
        break
    score += len(r)*len(r)
    for (x,y) in r:
        data[x][y]=-2
    for i in range(N-2,-1,-1):
        for j in range(N):
            if data[i][j]==-2 or data[i][j]==-1:
                continue
            for k in range(i+1,N):
                if data[k][j]==-2:
                    if k==N-1:
                        data[k][j]=data[i][j]
                        data[i][j]=-2
                    else:
                        continue
                else:
                    if k-1==i:
                        break
                    else:
                        data[k-1][j]=data[i][j]
                        data[i][j]=-2
                        break
    rotate=[[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            rotate[N-1-j][i]=data[i][j]
    data=rotate[:]
    for i in range(N-2,-1,-1):
        for j in range(N):
            if data[i][j]==-2 or data[i][j]==-1:
                continue
            for k in range(i+1,N):
                if data[k][j]==-2:
                    if k==N-1:
                        data[k][j]=data[i][j]
                        data[i][j]=-2
                    else:
                        continue
                else:
                    if k-1==i:
                        break
                    else:
                        data[k-1][j]=data[i][j]
                        data[i][j]=-2
                        break
print(score)
                        