#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int cnt = 1, hap = 0;
    while(cnt <= n) {
        if(n % cnt == 0)
            hap += cnt;
        cnt++;
    }
    return hap;
}