#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;
    for (int tc = 1; tc <= t; tc++){
        int n, m;
        cin >> n >> m;
        int snack[n];

        // 무게 입력
        for (int i = 0; i < n; i++) {
            cin >> snack[i];
        }

        // 최대 과자 구하기
        int maxSnack = 0;
        for (int i = 0; i < n - 1; i++)
        {
            for(int j = i + 1; j < n; j++) {
                int hap = snack[i] + snack[j];
                cout << snack[i] << " + " << snack[j] << " = " << hap << "\n";
                if (hap <= m)
                    maxSnack = (maxSnack <= hap) ? hap : maxSnack;
            }
        }
        if(maxSnack == 0)
            maxSnack = -1;
        cout << "#" << tc << " " << maxSnack << "\n";
    }
    return 0;
}
