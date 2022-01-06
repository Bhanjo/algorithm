#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;

    for (int tc = 1; tc<=t; tc++) {
        vector<int> arr(3);
        int time;
        for (int i = 0; i < arr.size(); i++)
            cin >> arr[i];
        if(arr[2] < arr[0])
            time = arr[0] - arr[2];
        else if(arr[2] > arr[1])
            time = -1;
        else
            time = 0;
        cout << "#" << tc << " " << time << "\n";
    }
    return 0;
}
