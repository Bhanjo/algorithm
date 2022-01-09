#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;
    for (int tc = 1; tc <= t; tc++) {
        int answer = 0;
        bool nowValue = false;
        string bit;
        cin >> bit;
        for (int i = 0; i < bit.length(); i++) {
            if((bit[i] - '0') != nowValue) {
                nowValue != nowValue;
                answer += 1;
            }
        }
        cout << "#" << tc << " " << answer << "\n";
    }
    return 0;
}
