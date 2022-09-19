#include <string>
#include <vector>

using namespace std;

string make2num(int k){
    string s="";
    while(1){
        int r = k %2;
        k = k/2;
        if(r==0)
            s=s+'0';
        else
            s=s+'1';
        if(k==0)
            break;
    }
    return s;
    
}
int countZero(string s){\
    int cnt =0;
    for(int i=0;i<s.size();i++){
        if(s[i]=='0')
            cnt++;
    }
    return cnt;                   
}

vector<int> solution(string s) {
    int zero_cnt = 0;
    int op =0;
    while(1){
        if(s.size()==1 && s[0]=='1')
            break;
        // check zero cnt
        int zc = countZero(s);
        zero_cnt += zc;
        // delete zero
        int cn = s.size() - zc;
        // change cn to 2
        string s1 = make2num(cn);
        s.clear();
        s="";
        for(int i=0;i<s1.size();i++){
            s=s+s1[i];
        }
        if(op==10)
            break;
        op++;
    }
    vector<int> answer;
    answer.push_back(op);
    answer.push_back(zero_cnt);
    return answer;
}