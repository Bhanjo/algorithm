// 콜라츠 추측
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solution(int num) {
  int answer = 0;
  int cnt = 0;
  while(cnt <= 500) {
    if(num == 1) {
      break;
    }
    num = (num % 2 == 0) ? num / 2 : num * 3 + 1;
    cout << "num : " << num << "\n";
    cnt += 1;
  }
  if(cnt <= 500)
    return cnt;
  return - 1;
}