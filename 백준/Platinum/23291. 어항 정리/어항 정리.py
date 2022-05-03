N,K= map(int,input().split())
data=list(map(int,input().split()))
#print(data)
mx=max(data)
mn=min(data)
if mx-mn<=K:
    print(0)
else:
    result=0
    while True:
        c=[]
        h=int(N/2)
        for i in range(h):
            if i==h-1:
                k=data[:]
                c.append(k)
            else:
                c.append([0 for _ in range(N)])

        # step1 : 물고기 넣기
        m = min(data)
        for i in range(N):
            if c[h-1][i] == m:
                c[h-1][i] += 1

        # step2: 왼쪽 어항 오른쪽 위
        c[h-2][1]=c[h-1][0]
        c[h-1][0]=0
        while True:
            mr=[]
            for i in range(N):
                if c[h-2][i]!=0:
                    mr.append(i)
            ml=len(mr)
            rot=[]
            rot_xy=[]
            for a in range(h):
                dd=[]
                for b in mr:
                    if c[a][b]!=0:
                        dd.append(c[a][b])
                        rot_xy.append((a,b))
                if len(dd)!=0:
                    rot.append(dd)
            start=0
            for i in range(N):
                if c[h-1][i] !=0:
                    start=i
                    break
            k= len(rot)
            for i in range(len(rot)):
                rot[i].reverse()
                for j in range(len(rot[i])):
                    c[h-2-j][start+k+len(rot[i])-1-i]=rot[i][j]
            for (x,y) in rot_xy:
                c[x][y]=0
            a=0
            b=0
            ddd=0
            for i in range(N):
                if c[h-2][i]==0:
                    if c[h-1][i]!=0:
                        a+=1
                else:
                    ddd=i
            for i in range(h):
                if c[i][ddd] !=0:
                    b+=1
            if b>a:
                break
        m_data=[item[:] for item in c]
        dx=[-1,0,1,0]
        dy=[0,1,0,-1]
        for x in range(h):
            for y in range(N):
                if c[x][y] !=0:
                    for i in range(4):
                        ax=x+dx[i]
                        ay=y+dy[i]
                        if ax<0 or ax>=h or ay<0 or ay>=N:
                            continue
                        if c[ax][ay]==0:
                            continue
                        if c[ax][ay]>c[x][y]:
                            m_data[x][y]+=(c[ax][ay]-c[x][y])//5
                            m_data[ax][ay]-=(c[ax][ay]-c[x][y])//5
        m_d=[]
        for y in range(N):
                if m_data[h-1][y]!=0:
                    for k in range(h-1,-1,-1):
                        if m_data[k][y]!=0:
                            m_d.append(m_data[k][y])
                        else:
                            break

        hm_d=m_d[:h]
        hm_d.reverse()
        hhm_d=m_d[(h):N]

        kd=[]
        kd.append(hm_d)
        kd.append(hhm_d)
        #print(kd)

        da=[]
        for i in range(1,-1,-1):
            bv=kd[i][:int(h/2)]
            bv.reverse()
            da.append(bv)
        for i in range(2):
            da.append(kd[i][int(h/2):N])
        fda=[item[:] for item in da]
        for x in range(3,-1,-1):
            for y in range(int(h/2)):
                for i in range(4):
                    ax=x+dx[i]
                    ay=y+dy[i]
                    if ax <0 or ay <0 or ax>=4 or ay >=int(h/2):
                        continue
                    if da[ax][ay] > da[x][y]:
                        fda[x][y] += (da[ax][ay] - da[x][y]) // 5
                        fda[ax][ay] -= (da[ax][ay] - da[x][y]) // 5
        final=[]
        for x in range(int(h/2)):
            for y in range(3,-1,-1):
                final.append(fda[y][x])
        #print(final)
        mx=max(final)
        mn=min(final)
        if mx-mn<=K:
            result +=1
            print(result)
            break
        else:
            result +=1
            data=final[:]
