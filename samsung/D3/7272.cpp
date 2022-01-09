#include <iostream>
#include <string>
using namespace std;

char zeroHole[19] = {
    'C', 'E', 'F', 'G',
    'H', 'I', 'J', 'K',
    'L', 'M', 'N', 'S',
    'T', 'U', 'V', 'W',
    'X', 'Y', 'Z'
};
char oneHole[6] = { 'A', 'D', 'O', 'P', 'Q', 'R' };

string result;
void isSame(char a, char b) {
    int howShowFirst, howShowSecond;
    for (char wordZeroHole : zeroHole) {
        if(wordZeroHole == a)
            howShowFirst = 1;
        if(wordZeroHole == b)
            howShowSecond = 1;
    }

    for (char wordOneHole : oneHole) {
        if(wordOneHole == a)
            howShowFirst = 2;
        if(wordOneHole == b)
            howShowSecond = 2;
    }

    if(a == 'B')
        howShowFirst = 3;
    if(b == 'B')
        howShowSecond = 3;

    if(howShowFirst != howShowSecond)
        result =  "DIFF";
}

int main() {
    int t;
    cin >> t;
    for (int tc = 1; tc <= t; tc++) {
        string first, second;
        cin >> first >> second;

        // 길이가 서로 다르면 오류
        if (first.length() != second.length())
            result = "DIFF";
        else {
            // 같은 분류인지 확인
            result = "SAME";
            for (int i = 0; i < first.length(); i++ ) {
                isSame(first[i], second[i]);
            }
        }
        cout << "#" << tc << " " << result << "\n";
    }
    return 0;
}
