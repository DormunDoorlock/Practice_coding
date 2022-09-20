#include <cstdio>
#include <string>

using namespace std;

int main(){
    string s="";
    int N,B;
    scanf("%d %d",&N,&B);
    while(1){
    	if(N==0)
        	break;
        int k=N%B;
        N=N/B;
        if(k<10)
            s=s+(char)(k+48);
        else{
            s=s+(char)(k+55);
        } 
    }
    for(int i=s.size()-1;i>=0;i--){
        printf("%c",s[i]);
    }
}