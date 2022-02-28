#include <string>
#include <vector>
#include <cmath>

using namespace std;

long long solution(long long n) {
    long long sq = sqrt(n);
    return pow(sq, 2) == n ? pow(sq + 1, 2) : -1;
}
