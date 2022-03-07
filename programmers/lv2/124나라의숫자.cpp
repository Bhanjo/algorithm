#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(int n) {
  string answer = "";
  int nameum = -1;
  while (n != 0) {
    nameum = n % 3;
    n /= 3;
    if (nameum == 0) {
      answer.append("4");
      n -= 1;
    }
    else if (nameum == 1)
      answer.append("1");
    else if (nameum == 2)
      answer.append("2");
  }
  reverse(answer.begin(), answer.end());
  return answer;
}