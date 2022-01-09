#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    int t;
    cin >> t;
    for (int tc = 1; tc <= t; tc++) {
        int len;
        cin >> len;
        vector<string> word(len);

        // 단어입력
        for (int i = 0; i < len; i++) {
            cin >> word[i];
        }

        // 셔플
        int mid = (len % 2 == 0) ? (len / 2) : (len / 2 + 1);
        vector<string> shuffleWord;
        for (int i = 0; i < mid; i++) {
            shuffleWord.push_back(word[i]);
            if(!(len % 2 == 1 && i == mid - 1))
                shuffleWord.push_back(word[i+mid]);
        }

        // 출력
        cout << "#" << tc << " ";
        for (int i = 0; i < len; i++) {
            cout << shuffleWord[i] << " ";
        }
        cout << "\n";
    }
    return 0;
}
