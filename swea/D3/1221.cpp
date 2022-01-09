#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    string viewNumber[10] = {"ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"};
    cin >> n;
    for (int tc = 1; tc <= n; tc++) {
        string case_num, str;
        vector<int> sortedNumber(10, 0);
        int len;
        cin >> case_num >> len;

        for (int i = 0; i < len; i++) {
            cin >> str;
            int num = find(viewNumber, viewNumber + 10, str) - viewNumber;
            sortedNumber[num] += 1;
        }

        cout << "#" << tc << "\n";
        for (int i = 0; i < 10; i++) {
            while (sortedNumber[i] != 0) { // 각 index 출력
                cout << viewNumber[i] << " ";
                sortedNumber[i] -= 1;
            }
        }
        cout << "\n";
    }
}
