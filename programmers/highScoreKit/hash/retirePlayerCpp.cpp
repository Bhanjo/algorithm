#include <string>
#include <vector>
#include <map>
using namespace std;

// 해시_완주하지 못한 선수
string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    map<string, int> hash;

    for (string s : completion)
    {
        hash[s] += 1;
    }
    for(string s : participant) {
        hash[s] -= 1;
        if(hash[s] < 0)
            return s;
    }
}
