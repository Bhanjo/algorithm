#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string s) {
  string answer = "";
  vector<char> words;

  while (!s.empty()) {
    words.push_back(s[s.length() - 1]);
    s.pop_back();
  }
  sort(words.begin(), words.end());

  while (!words.empty()) {
    answer.push_back(words[words.size() - 1]);
    words.pop_back();
  }
  return answer;
}

// best
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;

string solution(string s) {
  sort(s.begin(), s.end(), greater<char>());
  return s;
}