#include <string>
#include <vector>
using namespace std;

string solution(string s) {
    int index = 0;
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == ' ') {
            index = 0;
            continue;
        }

        // 홀수
        if (index % 2) {
            if (s[i] >= 'A' && s[i] <= 'Z')
                s[i] += 32;
        }
        else {
            if (s[i] >= 'a' && s[i] <= 'z')
                s[i] -= 32;
        }
        index += 1;
    }
    return s;
}