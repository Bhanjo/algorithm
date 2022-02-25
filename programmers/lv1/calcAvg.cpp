// 평균 구하기#include <string>
#include <vector>
#include <string>

using namespace std;

double solution(vector<int> arr) {
  double hap = 0;
  for (int i = 0; i < arr.size(); i++)
    hap += arr[i];
  return hap / arr.size();
}