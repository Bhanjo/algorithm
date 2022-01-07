#include <iostream>
#include <math.h>
using namespace std;

int human, top, ans;
int hap[21];

void dfs(int cnt, int height){
    if(cnt == human){
        if(height >= top)
            ans = min(ans, height);
        return;
    }
    dfs(cnt + 1, height + hap[cnt]); // 현재 키를 더했을 때
    dfs(cnt + 1, height); // 그냥 진행할 때
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;
    for (int tc = 1; tc <= n; tc++) {
        cin >> human >> top;
        for (int i = 0; i < human; i++)
            cin >> hap[i];

        ans = 10000000;
        dfs(0, 0);
        cout << "#" << tc << " " << ans - top << "\n";
    }
    return 0;
}
