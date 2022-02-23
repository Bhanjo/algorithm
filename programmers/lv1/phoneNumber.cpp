#include <string>
#include <vector>

using namespace std;

string solution(string phone_number) {
  string answer = "";
  int starCnt = 0;
  int i = 0;
  for (i = 0; i < phone_number.length(); i++) {
    starCnt += 1;

    if(phone_number.length() - starCnt < 4) {
      break;
    }
    answer.append("*");
  }

  for (i; i < phone_number.length(); i++) {
    answer.push_back(phone_number[i]);
  }

  return answer;
}

// best
string solution2(string phone_number) {
  string answer = "";
  for (int i = 0; i < phone_number.size() - 4; i++)
    phone_number[i] = '*';

  answer = phone_number;
  return answer;
}