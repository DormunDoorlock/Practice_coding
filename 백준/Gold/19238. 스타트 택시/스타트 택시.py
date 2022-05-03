from collections import deque

def BFS(graph,sx,sy,visited,cu,k,idex):
    result=[-1 for i in range(len(cu))]
    a=sx-1
    b=sy-1
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    queue=deque()
    queue.append((a,b))
    visited[a][b]=True
    for p in range(len(cu)):
        if a==cu[p][k]-1 and b==cu[p][k+1]-1:
            result[p]=0
    while queue:
        v = queue.popleft()
        #print(v,end='')
        for i in range(4):
            tx=v[0]+dy[i]
            ty=v[1]+dx[i]
            if tx>=len(graph) or ty>=len(graph) or tx<0 or ty<0 :
                continue
            elif visited[tx][ty] >0 or graph[tx][ty] == 1 :
                continue
            if idex==-1:
                for j in range(len(cu)):
                    if tx==cu[j][k]-1 and ty==cu[j][k+1]-1:
                        result[j]=visited[v[0]][v[1]]
                queue.append((tx,ty))
                visited[tx][ty] = visited[v[0]][v[1]] +1
            else:
                if tx==cu[index][k]-1 and ty==cu[index][k+1]-1:
                    visited[tx][ty] = visited[v[0]][v[1]]
                    return visited[tx][ty]
                else:
                    queue.append((tx,ty))
                    visited[tx][ty] = visited[v[0]][v[1]] +1
    if idex !=-1:
        return
    return result


N,M,fuel_cnt = map(int,input().split())
data=[]
for i in range(N):
    line=list(map(int,input().split()))
    data.append(line)

s_x,s_y=map(int,input().split())
customers=[]
for j in range(M):
    customer=list(map(int,input().split()))
    customers.append(customer)


cnt=0
while cnt<M:
    road=[]
    c=[]
    visited=[[0]*N for i in range(N)]
    road=BFS(data,s_x,s_y,visited,customers,0,-1)
    kk=0
    #print(road)
    for r in road:
        if r==-1:
            kk=1
            break
    if kk==1:
        break
    custom_fuel=min(road)
    for k in range(0,len(road)):
        if custom_fuel==road[k]:
            c.append((customers[k][0],customers[k][1]))
    #print(c)
    if len(c)==1:        
        index=road.index(custom_fuel)
    else:
        a=0
        x=c[0][0]
        y=c[0][1]
        for xi in range(1,len(c)):
            if x>c[xi][0]:
                x=c[xi][0]
                y=c[xi][1]
                a=xi
            elif x==c[xi][0]:
                if y>c[xi][1]:
                    x=c[xi][0]
                    y=c[xi][1]
                    a=xi
        for ab in range(len(customers)):
            if customers[ab][0]==x and customers[ab][1]==y:
                index=ab
    #print(customers[index])
    visited=[[0]*N for i in range(N)]
    if customers[index][0]== customers[index][2] and customers[index][1]==customers[index][3]:
        de_fuel=0
    else:
        de_fuel=BFS(data,customers[index][0],customers[index][1],visited,customers,2,index)
    if de_fuel==None:
        break
    #print(custom_fuel,de_fuel,index)
    max_fuel= custom_fuel + de_fuel
    if max_fuel>fuel_cnt:
        fuel_cnt=-1
        break
    else:
        fuel_cnt -= max_fuel
        fuel_cnt += de_fuel*2
        s_x=customers[index][2]
        s_y=customers[index][3]
        del customers[index]
        cnt+=1

if cnt != M:
    print(-1)
else:
    print(fuel_cnt)