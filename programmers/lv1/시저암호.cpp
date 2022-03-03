#include <string>
#include <vector>

using namespace std;

string solution(string s, int n) {
    string answer = "";
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == ' ') {
            answer.push_back(' ');
            continue;
        }
        int cnt = 0;
        char word = s[i];
        while (cnt < n) {
            word += 1;
            if (word > 'z')
                word = 'a';
            else if (word > 'Z' && word < 'a')
                word = 'A';
            cnt += 1;
        }
        answer.push_back(word);
    }
    return answer;
}