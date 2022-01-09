#include <iostream>
#include <vector>

using namespace std;

int main() {
    int t;
    cin >> t;
    for (int test_case = 1; test_case <= t; test_case++) {
        int m, n; // m = 영역, n = 파리채
        cin >> m >> n;
        int maxKill = 0;
        int moveCount = m - n + 1;

        vector<vector<int> > arr(m);
        vector<int> row(m);
        for (int i = 0; i < m; i++) { // 2차원 영역 입력
            for (int j = 0; j < m; j++)
                cin >> row[j];
            arr[i] = row;
        }

        // 출력
        for (int i = 0; i < moveCount; i++) {
            for (int j = 0; j < moveCount; j++) {
                int kill = 0;
                // n 파리채 내리치기
                for (int k = 0; k < n; k++) {
                    for (int q = 0; q < n; q++)
                        kill += arr[k + i][q + j];
                    if (kill >= maxKill)
                        maxKill = kill;
                }
            }
        }
        cout << "#" << test_case << " " << maxKill << endl;
    }
    return 0;
}
