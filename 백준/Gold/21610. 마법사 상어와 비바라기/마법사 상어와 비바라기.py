N,M=map(int,input().split())

data=[]
for _ in range(N):
    data.append(list(map(int,input().split())))
order=[]
for _ in range(M):
    order.append(list(map(int,input().split())))
cloud=[(N-1,0),(N-1,1),(N-2,0),(N-2,1)]

dx=[0,-1,-1,-1,0,1,1,1]
dy=[-1,-1,0,1,1,1,0,-1]

rdx=[-1,-1,1,1]
rdy=[-1,1,-1,1]
for o in order:
    d=o[0]-1
    num=o[1]
    rm=len(cloud)
    for i in range(len(cloud)):
        v=cloud[i]
        ax=v[0]+dx[d]*(num%N)
        ay=v[1]+dy[d]*(num%N)
        if ax < 0:
            ax +=N
        if ay < 0:
            ay +=N
        if ax >= N:
            ax -=N
        if ay >= N:
            ay -=N
        cloud.append((ax,ay))
    del cloud[:rm]
    co=[]
    for cl in cloud:
        if cl not in co:
            co.append(cl)
    cloud =co[:]
    for cl in cloud:
        data[cl[0]][cl[1]] +=1
    visited=[[0]*N for _ in range(N)]
    for cl in cloud:
        visited[cl[0]][cl[1]]=1
        for i in range(4):
            ax=cl[0]+rdx[i]
            ay=cl[1]+rdy[i]
            if ax < 0 or ay < 0 or ax >= N or ay >= N :
                continue
            if data[ax][ay]==0:
                continue
            data[cl[0]][cl[1]] +=1
    rmc = len(cloud)
    for x in range(N):
        for y in range(N):
            if data[x][y] >=2 :
                if visited[x][y]==0:
                    cloud.append((x,y))
                    data[x][y] -=2
    del cloud[:rmc]
result =0
for i in range(N):
    result += sum(data[i])
print(result)
    
    