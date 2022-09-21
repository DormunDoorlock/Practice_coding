#include <string>
#include <vector>

using namespace std;

int solution(vector<int> stones, int k) {
    int answer = 0;
    int left =1;
    int right=200000000;
    int mid;
    while(left<=right){
        mid = (left+right)/2;
        int cnt=0;
        int check=0;
        for(int i=0;i<stones.size();i++){
            if(stones[i]-mid<0){
                cnt++;
                if(cnt>=k){
                    check=1;
                    break;
                }
            }
            else{
                cnt=0;
            }
        }
        if(check==1){
            right=mid-1;
        }
        else{
            left=mid+1;
        }
    }
    answer=(left+right)/2;
    return answer;
}