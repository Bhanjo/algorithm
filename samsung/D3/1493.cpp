#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int arr[301][301];
    int num = 1;

    for (int i = 1; i < 301; i++) { // 배열 초기화
        arr[i][1] = num;
        for (int j = 2; j < 301; j++) {
            arr[i][j] = arr[i][j - 1] + i + j - 1;
        }
        num += i;
    }

    int n;
    cin >> n;

    for (int tc = 1; tc <= n; tc++) {
        int value1, value2, value1X, value1Y, value2X, value2Y;
        cin >> value1 >> value2;
        for (int i = 1; i < 301; i++) {
            for (int j = 1; j < 301; j++) {
                if(arr[i][j] == value1) {
                    value1X = i;
                    value1Y = j;
                }
                if(arr[i][j] == value2) {
                    value2X = i;
                    value2Y = j;
                }
            }
        }
        int result = arr[value1X + value2X][value1Y + value2Y];
        cout << "#" << tc << " " << result << "\n";
    }
    return 0;
}
