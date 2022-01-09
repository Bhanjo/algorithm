#include <iostream>
#include <string>
#include <sstream>
using namespace std;

// 글로벌 변수
int changeCount, maxPrice;
string price;

void dfs(int index, int current) {
    if(current == changeCount) {
        maxPrice = max(maxPrice, stoi(price));
        return;
    }
    for (int i = index; i < price.size() - 1; i++) {
        for (int j = i + 1; j < price.size(); j++) {
            swap(price[i], price[j]);
            dfs(i, current + 1);
            swap(price[i], price[j]);
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;
    for (int tc = 1; tc <= n; tc++) {
        cin >> price >> changeCount;
        maxPrice = 0;
        if(changeCount > price.size())
            changeCount = price.size();
        dfs(0, 0);
        cout << "#" << tc << " " << maxPrice << "\n";
    }
    return 0;
}
