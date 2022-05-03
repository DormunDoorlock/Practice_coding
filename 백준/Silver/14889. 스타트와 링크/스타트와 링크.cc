#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
int num=0;
int arr[21][21];
int arr1[21];
int start[11];
int link[11];
vector<int> v;
int check(){
    int as=0;
    int al=0;
    for(int i=0;i<num/2-1;i++){
        for(int j=i+1;j<num/2;j++){
            as+=arr[start[i]-1][start[j]-1]+arr[start[j]-1][start[i]-1];
            al+=arr[link[i]-1][link[j]-1]+arr[link[j]-1][link[i]-1];
        }
    }
    if(as>al)
        return(as-al);
    else
        return(al-as);
}
void com(int a,int b){
    if(b>=num/2){
        if(start[num/2-1]==0)
            return;
        int pos=0;
        for(int i=0;i<num;i++){
            int qw=0;
            for(int j=0;j<num/2;j++){
                if(arr1[i]==start[j]) {
                    qw = 1;
                    //printf(" %d %d ",i,j);
                    break;
                }
            }
            if(qw==0){
                link[pos]=arr1[i];
                pos++;
            }
        }
        v.push_back(check());
        return;
    }
    if(a>num)
        return;
    start[b]=arr1[a];
    com(a+1,b+1);
    com(a+1,b);
}
int main(){
    scanf("%d",&num);
    for(int i=0;i<num;i++){
        for(int j=0;j<num;j++){
            int a;
            scanf("%d",&a);
            arr[j][i]=a;
        }
    }
    for(int i=0;i<num;i++){
        arr1[i]=i+1;
    }
    com(0,0);
    sort(v.begin(),v.end());
    printf("%d",v[0]);
    return 0;
}