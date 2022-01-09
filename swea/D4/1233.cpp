#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    for (int tc = 1; tc <= 10; tc++) {
        int len, result = 1;
        cin >> len;
        for (int i = 1; i <= len; i++) {
            char cal;
            cin >> i >> cal;

            if(i <= len / 2) { // 부모 노드일때
                int left, right;
                if(i == len / 2 && len % 2 == 0) // 가장 마지막 부모 노드
                    cin >> left;
                else
                    cin >> left >> right;
                if(cal >= '0' && cal <= '9') // 숫자일때(연산자가 와야함)
                    result = 0;
            } else { // 자식 노드일때
                if(!(cal >= '0' && cal <= '9')) // 숫자가 아닐때
                    result = 0;
            }
        }
        cout << "#" << tc << " " << result << "\n";
    }
    return 0;
}
