#include <iostream>
#include <queue>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    for (int tc = 1; tc <= 10; tc++) {
        queue<int> q;
        int t;
        cin >> t;

        // 큐에 8개 숫자 입력
        for (int i = 0; i < 8; i++) {
            int num;
            cin >> num;
            q.push(num);
        }

        // 검사 시작
        int decrease = 1;
        while (true)
        {
            // 큐에서 pop하여 계산 후 뒤에 붙이기
            int num;
            int cal = q.front() - decrease;
            num = (cal < 0) ? 0 : cal;
            q.pop();
            q.push(num);

            // 뒤가 0인지 판단
            if(q.back() <= 0) {
                // 프린트 후 종료
                cout << "#" << t << " ";
                while(!q.empty()) {
                    cout << q.front() << " ";
                    q.pop();
                }
                cout << "\n";
                break;
            }
            decrease = (decrease >= 5) ? 1 : (decrease + 1);
        }
    }
}
