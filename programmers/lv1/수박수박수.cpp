#include <string>
#include <vector>

using namespace std;

string solution(int n) {
    string answer = "";
    int cnt = n / 2;
    for (int i = 0; i < cnt; i++) {
        answer.append("수박");
    }
    if (n % 2 == 1) answer.push_back('수');
    return answer;
}

// 다른 풀이
string solution(int n) {
    string answer = "";

    for (int i = 0; i < n; i++)
        i & 1 ? answer += "박" : answer += "수";

    return answer;
}