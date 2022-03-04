#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> arr)
{
  vector<int> answer;
  int temp = 1000001;
  for (int i = 0; i < arr.size(); i++) {
    if (arr[i] != temp) {
      answer.push_back(arr[i]);
      temp = arr[i];
    }
  }

  return answer;
}

// best
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

vector<int> solution(vector<int> arr)
{
  arr.erase(unique(arr.begin(), arr.end()), arr.end());
  vector<int> answer = arr;
  return answer;
}