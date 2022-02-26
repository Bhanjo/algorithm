// 최소공배수와 최대공약수
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int gcd(int n, int m) {
	if (m == 0)
		return n;
	else
		return gcd(m, n % m);
}

vector<int> solution(int n, int m) {
	vector<int> answer;
	int maxNum = gcd(n, m);
	answer.push_back(maxNum);
	answer.push_back(n * m / maxNum);
	return answer;
}

int main() {
	vector<int> test = solution(5, 12);
	for (int i = 0; i < test.size(); i++) {
		cout << test[i] << " ";
	}
	cout << "\n";
}