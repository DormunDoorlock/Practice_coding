#include <string>
#include <vector>
#include <map>
using namespace std;
map<long ,long> m;

long long ck(long long b){
    if(!m[b]==true)
        return b;
    return m[b]=ck(m[b]);
}
vector<long long> solution(long long k, vector<long long> room_number) {
    vector<long long> answer;
    for(long long i=0;i<room_number.size();i++){
        if(!m[room_number[i]]==true){
            answer.push_back(room_number[i]);
            m[room_number[i]]=ck(room_number[i]+1);
        }
        else{
            long long check=ck(room_number[i]);
            answer.push_back(check);
            m[check]=ck(check+1);
        }
    }
    return answer;
}