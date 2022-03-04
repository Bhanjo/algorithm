#include <string>
#include <vector>
#include <algorithm>

using namespace std;
int N;

bool comp(string s1, string s2) {
  if (s1[N] == s2[N]) return s1 < s2;
  return s1[N] < s2[N];
}

vector<string> solution(vector<string> s, int n) {
  N = n;
  sort(s.begin(), s.end(), comp);
  return s;
}