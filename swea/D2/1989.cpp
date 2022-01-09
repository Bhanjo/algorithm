#include <iostream>

using namespace std;

int main() {
    int t;
    cin >> t;
    for (int test_case = 1; test_case <= t; test_case++) {
        string str;
        int isCorrect = 1;
        cin >> str;

        // 회문 판별
        int reverse = str.length() - 1;
        for (int i = 0; i < str.length() / 2; i++) {
            if (str[i] != str[reverse]) {
                isCorrect = 0;
                break;
            }
            reverse -= 1;
        }
        cout << "#" << test_case << " " << isCorrect << endl;
    }
    return 0;
}
