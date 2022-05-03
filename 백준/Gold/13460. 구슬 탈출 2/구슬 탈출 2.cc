#include <cstdio>
#include <queue>
using namespace std;
int answer;
int gx,gy;
int n1,n2;
int ax,ay;
int cx,cy;
char arr[10][10];
bool checked[11][11][11][11];

typedef struct _ck{
    int rx=0;
    int ry=0;
    int bx=0;
    int by=0;
    int num=0;
} ck;
void bfs() {
    int mx[4]={-1,0,1,0};
    int my[4]={0,-1,0,1};
    queue<ck> q;
    ck c;
    c.rx=ax;
    c.ry=ay;
    c.bx=cx;
    c.by=cy;
    c.num=0;
    q.push(c);
    checked[ax][ay][cx][cy]=true;
    while(!q.empty()){
        int z=q.front().rx;
        int w=q.front().ry;
        int e=q.front().bx;
        int r=q.front().by;
        int l=q.front().num;

        q.pop();
        // printf("%d %d %d %d\n",z,w,e,r);
        if(l>10){
            answer=-1;
            return;
        }
        if(arr[z][w]=='O'){
            if(l<=10){
                answer=l;
                return;
            }
            else{
                return;
            }
        }

        for(int i=0;i<4;i++){
            int nz=z;
            int nw=w;
            int ne=e;
            int nr=r;
            while(true){
                if(arr[nz+mx[i]][nw+my[i]]=='#' || arr[nz+mx[i]][nw+my[i]]=='O')
                    break;
                nz=nz+mx[i];
                nw=nw+my[i];
            }
            if(arr[nz+mx[i]][nw+my[i]]=='O'){
                nz=nz+mx[i];
                nw=nw+my[i];
            }
            while(true){
                if(arr[ne+mx[i]][nr+my[i]]=='#'||arr[ne+mx[i]][nr+my[i]]=='O')
                    break;
                ne=ne+mx[i];
                nr=nr+my[i];
            }
            if(arr[ne+mx[i]][nr+my[i]]=='O'){
                continue;
            }
            if(arr[ne][nr]=='#') {
                ne = ne - mx[i];
                nr = nr - my[i];
            }
            if(nz==ne && nw==nr ){
                if(arr[nz][ne]=='O')
                    continue;
                if(i==0){
                    if(z<e)
                        ne++;
                    else
                        nz++;
                }
                if(i==1){
                    if(w<r)
                        nr++;
                    else
                        nw++;
                }
                if(i==2){
                    if(z<e)
                        nz--;
                    else
                        ne--;
                }
                if(i==3){
                    if(w<r)
                        nw--;
                    else
                        nr--;
                }
            }
            if(checked[nz][nw][ne][nr]==false){
                checked[nz][nw][ne][nr]=true;
                ck nc;
                nc.rx=nz;
                nc.ry=nw;
                nc.bx=ne;
                nc.by=nr;
                nc.num=l+1;
                q.push(nc);
            }
        }
    }
}
int main() {
    scanf("%d %d",&n1,&n2);
    for(int i=0;i<n1;i++){
        for(int j=0;j<n2;j++){
            char a;
            scanf("%c",&a);
            if(a=='\n')
                scanf("%c",&a);
            arr[i][j] = a;
            if(a=='R'){
                ax=i;
                ay=j;
            }
            if(a=='B'){
                cx=i;
                cy=j;
            }
            if(a=='O'){
                gx=i;
                gy=j;
            }
        }
    }

    bfs();
    if(answer==0)
        printf("-1");
    else
        printf("%d",answer);

    return 0;

}