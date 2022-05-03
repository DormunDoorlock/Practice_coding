N , M = map(int,input().split())

data=[]
for _ in range(N):
    data.append(list(map(int,input().split())))
order=[]
for _ in range(M):
    order.append(list(map(int,input().split())))

start = int((N+1)/2) -1
dx=[-1,1,0,0]
dy=[0,0,-1,1]

rdx=[0,1,0,-1]
rdy=[-1,0,1,0]

visited=[[0]*N for _ in range(N)]
visited[start][start]=1
x , y = start,start
dxy=0
rxy=1
dorder=[]
result1=0
result2=0
result3=0
while True:
    dorder.append((x,y))
    if x==0 and y==0 :
        break
    ax=x+rdx[dxy]
    ay=y+rdy[dxy]

    rx=ax+rdx[rxy]
    ry=ay+rdy[rxy]

    if visited[rx][ry]==0:
        dxy =rxy
        rxy = (rxy+1)%4
        visited[x][y]=1
        x=ax
        y=ay
    else:
        visited[x][y]=1
        x=ax
        y=ay
            
for o in order:
    di=o[0]-1
    n=o[1]
    dt=[]
    for i in range(1,n+1):
        data[start+dx[di]*i][start+dy[di]*i]=-1
        dt.append((start+dx[di]*i,start+dy[di]*i))
    for do in range(len(dorder)):
        if data[dorder[do][0]][dorder[do][1]] == -1:
            for k in range(do,len(dorder)-1):
                data[dorder[k][0]][dorder[k][1]]=data[dorder[k+1][0]][dorder[k+1][1]]
            data[0][0]=0
    while True:
        group=[]
        gg=[]
        for do in range(1,len(dorder)-1):
            v=dorder[do]
            nv=dorder[do+1]
            if data[v[0]][v[1]] ==0:
                break
            if data[v[0]][v[1]] == data[nv[0]][nv[1]]:
                gg.append(v)
            else:
                if len(gg)>=3:
                    gg.append(v)
                    group.append(gg[:])
                    gg.clear()
                if len(gg)==1 or len(gg)==2:
                    gg.clear()
        group.reverse()
        for g in group:
            k=len(g)
            v=g[0]
            result =data[v[0]][v[1]]
            if result ==1:
                result1 += k
            elif result ==2:
                result2 += k
            elif result ==3:
                result3 += k
            st=dorder.index(v)
            for z in range(st,len(dorder)-k):
                data[dorder[z][0]][dorder[z][1]]=data[dorder[z+k][0]][dorder[z+k][1]]
            
        if len(group)==0:
            break    
    n_data=[[0]*N for _ in range(N)]
    i=1
    for j in range(1,len(dorder)-1,1):
        if i >= len(dorder):
            break
        if  data[dorder[j][0]][dorder[j][1]]==0:
            break
        if data[dorder[j][0]][dorder[j][1]]==data[dorder[j-1][0]][dorder[j-1][1]]:
            continue
        if data[dorder[j][0]][dorder[j][1]]==data[dorder[j+1][0]][dorder[j+1][1]] and data[dorder[j+1][0]][dorder[j+1][1]]==data[dorder[j+2][0]][dorder[j+2][1]]: 
            n_data[dorder[i][0]][dorder[i][1]]=3
            n_data[dorder[i+1][0]][dorder[i+1][1]]=data[dorder[j][0]][dorder[j][1]]
            i +=2
        elif data[dorder[j][0]][dorder[j][1]]==data[dorder[j+1][0]][dorder[j+1][1]]:
            n_data[dorder[i][0]][dorder[i][1]]=2
            n_data[dorder[i+1][0]][dorder[i+1][1]]=data[dorder[j][0]][dorder[j][1]]
            i +=2
        else:
            n_data[dorder[i][0]][dorder[i][1]]=1
            n_data[dorder[i+1][0]][dorder[i+1][1]]=data[dorder[j][0]][dorder[j][1]]
            i +=2
    
    data=n_data[:]
                
        
print(1*result1+2*result2+3*result3)
       