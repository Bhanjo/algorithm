#include <string>
#include <iostream>
using namespace std;

bool solution(string s)
{
  int cntP = 0, cntY = 0;
  for (int i = 0; i < s.length(); i++) {
    if (s[i] == 'p') cntP += 1;
    if (s[i] == 'y') cntY += 1;
  }
  return cntP == cntY? true:false;
}