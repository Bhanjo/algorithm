#include <string>
#include <vector>
using namespace std;

string solution(string s) {
  string answer = "";
  if (s.length() % 2 == 0) {
    answer.push_back(s[s.length() / 2 - 1]);
    answer.push_back(s[s.length() / 2]);
  }
  else
    answer.push_back(s[s.length() / 2]);
  return answer;
}

// best
#include <string>
#include <vector>
using namespace std;

string solution(string s) {
  int len = s.length();
  if (len % 2 == 0)
  {
    return s.substr(len / 2 - 1, 2);
    }
    else {
            return s.substr(len/2,1);
        }
}