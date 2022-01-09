#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;

    for (int tc = 1; tc <= t; tc++) {
        vector<string> arr(5);
        // 문자열 입력
        for (int i = 0; i < 5; i++)
            cin >> arr[i];
        // 새로로 읽기
        vector<char> word;
        for (int y = 0; y < 15; y++) {
            for (int x = 0; x < 5; x++) {
                if(arr[x].size() > y)
                    word.push_back(arr[x][y]);
            }
        }
        // 출력
        cout << "#" << tc << " ";
        for (int i = 0; i < word.size(); i++)
            cout << word[i];
        cout << "\n";
    }
    return 0;
}
