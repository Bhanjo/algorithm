// 짝수와 홀수
#include <string>
#include <vector>
using namespace std;

string solution(int num) {
	string answer = num % 2 == 0 ? "Even" : "Odd";
	return answer;
}