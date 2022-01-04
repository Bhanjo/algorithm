#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char** argv) {
    int test_case;
    int T;
    cin >> T;
    for (test_case = 1; test_case <= T; ++test_case) {
        int a, b;
        int max = 0;
        cin >> a >> b;
        vector<int> arr1(a), arr2(b), low, high;

        for (int i = 0; i < a; i++)
            cin >> arr1[i];
        for (int i = 0; i < b; i++)
            cin >> arr2[i];

        if(arr1.size() <= arr2.size()) {
            low = arr1;
            high = arr2;
        } else {
            low = arr2;
            high = arr1;
        }

        for (int i = 0; i <= high.size() - low.size(); i++) {
            int value = 0;
            for (int j = 0; j < low.size(); j++) {
                value += low[j] * high[j + i];
            }
            if(value >= max)
                max = value;
        }
        cout << "#" << test_case << " " << max << endl;
    }
    return 0;
}
