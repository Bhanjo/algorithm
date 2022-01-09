#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    int t;
    cin >> t;
    for (int tc = 1; tc <= t; tc++) {
        int n;
        cin >> n;
        vector<vector<int> > arr(n);

        // 배열 입력
        string arrX;
        getline(cin, arrX); // 첫 개행문자 무시
        for (int i = 0; i < n; i++) {
            getline(cin, arrX);
            for (int j = 0; j < arrX.size(); j++) {
                int num = arrX[j] - '0';
                arr[i].push_back(num);
            }
        }

        // 가치 구하기
        int mid = n / 2;
        int value = 0;
        int count = 0;
        for (int x = 0; x < n; x++) {
            for (int y = mid - count; y <= mid + count; y++) {
                value += arr[x][y];
            }
            count = (x >= mid) ? count -= 1 : count += 1;
        }
        cout << "#" << tc << " " << value << "\n";
    }
    return 0;
}
