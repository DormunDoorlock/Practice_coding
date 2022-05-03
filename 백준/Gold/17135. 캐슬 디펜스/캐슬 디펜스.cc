#include <cstdio>
#include <set>
#include <vector>
#include <algorithm>
using namespace std;
int arr[15][15];
int n,m,d;
int as[15][15];
set <pair<int,int>> s;
typedef struct _pos{
    int x=0;
    int y=0;
    int z=0;
}pos;
bool incheck(int o,int p){
    return((o>=0 && o<n)&&(p>=0 && p<m));
}
void ckck(int na,int cx){
    int k=1;
    while(1) {
        if(k>d){
            return;
        }
        for (int i = 1; i <= k; i++) {
            int ax = n - i - na;
            int ay = cx - k + i;
            if (incheck(ax, ay)) {
                if (arr[ax][ay] == 1) {
                    if(s.insert(make_pair(ax,ay)).second==false) {
                        if(as[ax][ay]==na)
                            return;
                        else
                            continue;
                    }
                    else {
                        s.insert(make_pair(ax,ay));
                        as[ax][ay]=na;
                        return;
                    }
                }
                else
                    continue;
            }
        }
        for (int i = 1; i < k; i++) {
            int aax = n - k + i - na;
            int aay = cx + i;
            if (incheck(aax, aay)) {
                if(arr[aax][aay]==1){
                    if(s.insert(make_pair(aax,aay)).second==false) {
                        if (as[aax][aay] == na)
                            return;
                        else
                            continue;
                    }
                    else {
                        s.insert(make_pair(aax,aay));
                        as[aax][aay]=na;
                        return;
                    }
                }
                else
                    continue;
            }
        }
        k++;
    }
}
void check(pos ps){
    int na=0;
    int cx=ps.x;
    int cy=ps.y;
    int cz=ps.z;
    while(true){
        if(na==n)
            break;
        ckck(na,cx);
        ckck(na,cy);
        ckck(na,cz);
        na++;
    }
}

int main(){
    scanf("%d %d %d",&n,&m,&d);
    vector<int>answer;
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            int a=0;
            scanf("%d",&a);
            arr[i][j]=a;
        }
    }
    answer.clear();
    for(int a=0;a<=m-3;a++){
        for(int b=a+1;b<=m-2;b++){
            for(int c=a+2;c<=m-1;c++){
                if(b>=c)
                    continue;
                pos p;
                p.x=a;
                p.y=b;
                p.z=c;
                check(p);
                answer.push_back(s.size());
                s.clear();
                for(int i=0;i<n;i++){
                    for(int j=0;j<m;j++){
                        as[i][j]=-1;
                    }
                }
            }
        }
    }


   int max=*max_element(answer.begin(),answer.end());
    printf("%d",max);

}