#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    for (int tc = 1; tc <= t; tc++) {
        int n;
        cin >> n;
        vector<int> arr(n);
        for (int i = 0; i < arr.size(); i++) // 높낮이 입력
            cin >> arr[i];

        int upMax = 0, downMax = 0;
        if(arr.size() > 2) {
            for (int i = 1; i < arr.size() - 1; i++) {
                if(arr[i] - arr[i-1] >= upMax)
                    upMax = arr[i] - arr[i - 1];
                else if(arr[i] - arr[i-1] < 0)
                    downMax = (downMax <= -(arr[i] - arr[i - 1])) ? -(arr[i] - arr[i - 1]) : downMax;
                if (arr[i] - arr[i + 1] >= downMax)
                    downMax = arr[i] - arr[i + 1];
                else if(arr[i] - arr[i+1] < 0)
                    upMax = (upMax <= -(arr[i] - arr[i + 1])) ? -(arr[i] - arr[i + 1]) : upMax;
            }
        } else {
            if(arr[1] - arr[0] >= 0)
                upMax = arr[1] - arr[0];
            else
                downMax = -(arr[1] - arr[0]);
        }

        cout << "#" << tc << " " << upMax << " " << downMax << "\n";
    }
    return 0;
}
