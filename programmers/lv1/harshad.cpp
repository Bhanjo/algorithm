// 하샤드수
#include <string>
#include <vector>

using namespace std;

bool solution(int x) {
  int digit = 10000, num = x, hap = 0;
  while(true) {
    hap += num / digit;
    num %= digit;
    if(num < 10) {
      hap += num;
      break;
    }
    digit = digit / 10;
  }
  return x % hap == 0 ? true : false;
}