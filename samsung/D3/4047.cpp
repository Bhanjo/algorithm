#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;
    for (int tc = 1; tc <= t; tc++) {
        bool isError = false;
        int needCard[4] = {13, 13, 13, 13};
        int existCard[4][13] = {
            {0,0,0,0,0,0,0,0,0,0,0,0,0},
            {0,0,0,0,0,0,0,0,0,0,0,0,0},
            {0,0,0,0,0,0,0,0,0,0,0,0,0},
            {0,0,0,0,0,0,0,0,0,0,0,0,0},
        };
        string myCard;
        cin >> myCard;
        int cardNum;

        for (int i = 0; i < myCard.length(); i++) {
            int needCardIndex;
            if(i % 3 == 0) {
                // 카드가 알파벳이면
                cardNum = 0;
                if(myCard[i] == 'S')
                    needCardIndex = 0;
                else if(myCard[i] == 'D')
                    needCardIndex = 1;
                else if(myCard[i] == 'H')
                    needCardIndex = 2;
                else if(myCard[i] == 'C')
                    needCardIndex = 3;
            } else if(i % 3 == 1) {
                // 10의 자리 숫자 일때
                if(myCard[i] == '1')
                    cardNum += 10;
            } else if(i % 3 == 2) {
                // 1의 자리 숫자일때
                cardNum += myCard[i] - '0';
                if(existCard[needCardIndex][cardNum - 1] > 0) {
                    cout << "#" << tc << " ERROR\n";
                    isError = true;
                }
                else {
                    existCard[needCardIndex][cardNum - 1] += 1;
                    needCard[needCardIndex] -= 1;
                }
            }
        }
        if(!isError) {
            cout << "#" << tc;
            for (int i = 0; i < 4; i++) {
                cout << " " << needCard[i];
            }
            cout << "\n";
        }
    }
    return 0;
}
