#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    for (int tc = 1; tc <= 10; tc++) {
        int countTraffic = 0; // 교착상태 카운트
        int size;
        cin >> size;
        char field[100][100];

        // (0: 빈칸, 1: N, 2: S), (위: N, 아래: S)
        for (int i = 0; i < 100; i ++) {
            for (int j = 0; j < 100; j++)
                cin >> field[i][j];
        }

        for (int y = 0; y < 100; y++) {
            char prev = '0';
            for (int x = 0; x < 100; x++) {
                if(field[x][y] == '1') {
                    prev = '1';
                } else if(field[x][y] == '2'){
                    if(prev == '1') {
                        countTraffic += 1;
                        prev = '2';
                    }
                }
            }
        }
        cout << "#" << tc << " " << countTraffic << '\n';
    }
    return 0;
}
