#include <iostream>
#include <vector>
#include <utility>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    vector<pair<int, int> > v;
    int n;
    cin >> n;

    // 풍선 입력
    for (int i = 1; i <= n; i++)
    {
        int moveCount = 0;
        cin >> moveCount;
        v.push_back(make_pair(i, moveCount));
    }

    while(!v.empty()) {
        cout << v.front().first << " ";
        int moveTo = v.front().second;
        v.erase(v.begin());
        if(v.empty())
            return 0;

        // 터져야할 풍선을 맨 앞으로 가져온다
        if(moveTo > 0) {
            for (int i = 0; i < moveTo - 1; i++) {
                v.push_back(v.front());
                v.erase(v.begin());
            }
        } else {
            for (int i = 0; i < abs(moveTo); i++) {
                v.insert(v.begin(), v.back());
                v.erase(v.end()-1);
            }
        }
    }
}
