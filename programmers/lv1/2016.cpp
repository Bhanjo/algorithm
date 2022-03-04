#include <string>
#include <vector>
#include <ctime>

using namespace std;

string solution(int a, int b) {
  string days[7] = {"SUN","MON","TUE","WED","THU","FRI","SAT"};
  int month[12] = { 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };

  int sum = 0;
  for(int i = 1; i < a; i++)
    sum += month[i - 1];
  sum += b - 1;

  return days[(5 + sum) % 7];
}