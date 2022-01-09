#include <iostream>
using namespace std;

int n, k, answer;
int arr[20];

void hap(int index, int sum) {
    if(sum > k)
        return;

    if(sum == k) {
        answer += 1;
        return;
    }

    for(int i = index; i < n; i++)
        hap(i + 1, sum + arr[i]);
}

int main() {
    int round;
    cin >> round;
    for (int tc = 1; tc <= round; tc++) {
        n = 0, k = 0, answer = 0;
        cin >> n >> k;
        for (int i = 0; i < n; i++)
            cin >> arr[i];
        hap(0, 0);
        cout << "#" << tc << " " << answer << "\n";
    }
    return 0;
}
