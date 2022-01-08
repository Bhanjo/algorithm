#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;

    for (int tc = 1; tc <= t; tc++) {
        int n, m; // n = 주차장 수, m = 들어올 차량 수
        int hap = 0;
        vector<int> parking(n);
        cin >> n >> m;

        // 주차장 요금, 차량입출 입력
        int garagePrice[n];
        for (int i = 0; i < n; i++)
            cin >> garagePrice[i];

        // 차량 무게 입력
        int cars[m];
        for (int j = 0; j < m; j++)
            cin >> cars[j];

        for (int i = 0; i < n; i++) {
            parking.push_back(0);
        }

        // 차량 입출 입력
        int inputCar;
        vector<int> waitCar;
        for (int i = 0; i < 2 * m; i++)
        {
            cin >> inputCar;
            // 입차
            if (inputCar >= 1 && inputCar <= 9) {
                int isPosible = 0;
                for (int i = 0; i < n; i++) {
                    // 자리가 있다면
                    if(parking[i] == 0) {
                        cout << "최초입차" << i << " : " << cars[inputCar-1] <<  "\n";
                        parking[i] = inputCar;
                        isPosible = 1;
                        break;
                    }
                }
                // 자리가 없다면
                if (isPosible == 0) {
                    waitCar.push_back(inputCar);
                }
            }
            else if (inputCar < 0) {
                // 출차할 차의 위치 찾기
                int index = find(parking.begin(), parking.end(), -1 * inputCar) - parking.begin();
                parking[index] = 0;
                hap += garagePrice[index] * cars[(inputCar * -1) - 1];

                // 대기중인 자동차 있으면 해당 위치에 넣기
                if (!waitCar.empty()) {
                    parking[index] = waitCar[0];
                    waitCar.erase(waitCar.begin());
                }
            }
        }
        cout << "#" << tc << " " << hap << "\n";
    }
    return 0;
}

// #include <iostream>
// #include <vector>
// #include <queue>
// using namespace std;

// int main() {
// 	ios_base::sync_with_stdio(false);
// 	cin.tie(NULL);
// 	cout.tie(NULL);
// 	int T;
// 	cin >> T;
// 	for (int i = 1; i <= T; i++) {
// 		int sum = 0, n, m;
// 		cin >> n >> m;

// 		priority_queue<int, vector<int>, greater<int>> available_pos;//주차가능 자리(번호 낮은순으로 정렬)
// 		vector <int> parking_charge(n); //주차 자리별 요금
// 		for (int j = 0; j < n; j++) {
// 			cin >> parking_charge[j];
// 			available_pos.push(j);
// 		}

// 		vector <pair<int, int>> car_info(m + 1); // <무게, 주차한 자리>
// 		int w;
// 		for (int j = 1; j <= m; j++) {
// 			cin >> w;
// 			car_info[j] = make_pair(w, -1);
// 		}

// 		int car_input;
// 		queue <int> waiting_cars; //주차 대기 차량(먼저 온 차 우선)
// 		for (int j = 0; j < m * 2; j++) {
// 			cin >> car_input;
// 			if (car_input > 0)
// 				waiting_cars.push(car_input);
// 			else if (car_input < 0)
// 				available_pos.push(car_info[car_input * -1].second);

// 			//주차 대기 차량과 주차 자리가 있다면 주차시킴
// 			while (waiting_cars.size() > 0 && available_pos.size() > 0) {
// 				int pos = available_pos.top();
// 				available_pos.pop();
// 				int car = waiting_cars.front();
// 				waiting_cars.pop();
// 				sum += car_info[car].first * parking_charge[pos];
// 				car_info[car].second = pos;
// 			}
// 		}
// 		cout << "#" << i << " " << sum <<  "\n";
// 	}
// 	return 0;
// }
