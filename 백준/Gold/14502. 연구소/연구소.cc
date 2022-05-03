#include <cstdio>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
vector< vector <int>> checked;
vector< vector <int>> start;
int n,m;
int what=0;
int bfs(){
    queue<pair<int,int>> og;
    queue<pair<int,int>> q;
    for(int u=0;u<m;u++){
        for(int l=0;l<n;l++){
            checked[u][l]=0;
            if(start[u][l]==2){
                og.push(make_pair(u,l));
                q.push(make_pair(u,l));
                checked[u][l]=1;
            }
        }
    }
    while(true){
        int x=q.front().first;
        int y=q.front().second;
        if(q.empty()){
            break;
        }
        q.pop();
        if (x + 1 < m) {
            if (start[x + 1][y] == 0 && checked[x + 1][y] == 0){
                q.push(make_pair(x+1,y));
                start[x + 1][y] = 2;
                checked[x+1][y]=1;
            }
        }
        if (x - 1 >= 0) {
            if (start[x - 1][y] == 0 && checked[x - 1][y] == 0) {
                q.push(make_pair(x-1,y));
                start[x - 1][y] = 2;
                checked[x-1][y]=1;
            }
        }
        if (y + 1 < n) {
            if (start[x][y + 1] == 0 && checked[x][y + 1] == 0) {
                q.push(make_pair(x,y+1));
                start[x][y + 1] =2;
                checked[x][y+1]=1;
            }
        }
        if (y - 1 >= 0) {
            if (start[x][y - 1] == 0 && checked[x][y - 1] == 0) {
                q.push(make_pair(x,y-1));
                start[x][y - 1] =2;
                checked[x][y-1]=1;
            }
        }
    }
    what=0;
    for(int o=0;o<m;o++){
        for(int p=0;p<n;p++) {
            if(start[o][p]==0)
                what++;
            if(start[o][p]==2)
                start[o][p]=0;
        }
    }

    while(true){
        if(og.empty())
            break;

        int ox=og.front().first;
        int oy=og.front().second;
        og.pop();
        start[ox][oy]=2;
    }
    return what;
}
int main() {
    int a;
    int answer=0;
    vector<pair<int,int>> vp;
    vector<int> arr;
    checked.clear();
    start.clear();
    scanf("%d %d",&m,&n);
    checked.resize(m,vector<int>(n,0));
    start.resize(m,vector<int>(n,0));
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            scanf("%d",&a);
            start[i][j]=a;
            if(a==0) {
                vp.push_back(make_pair(i, j));
            }
        }
    }
    for(int b=0;b<=vp.size()-3;b++){
        for(int c=b+1;c<=vp.size()-2;c++){
            for(int d=c+1;d<=vp.size()-1;d++){
                answer=0;
                start[vp[b].first][vp[b].second]=1;
                start[vp[c].first][vp[c].second]=1;
                start[vp[d].first][vp[d].second]=1;
                answer=bfs();
                arr.push_back(answer);
                start[vp[b].first][vp[b].second]=0;
                start[vp[c].first][vp[c].second]=0;
                start[vp[d].first][vp[d].second]=0;
            }
        }
    }
    sort(arr.begin(),arr.end(),greater<int>());
    printf("%d",arr[0]);




}
