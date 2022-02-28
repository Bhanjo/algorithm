#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

long long solution(long long n) {
    long long answer = 0;
    long long cnt = 10;
    vector<long long> nums;

    // 자릿수별로 저장
    while (n) {
        nums.push_back(n % cnt);
        n /= cnt;
    }

    sort(nums.begin(), nums.end());
    long long digit = 1;
    for (int i = 0; i < nums.size(); i++) {
        answer += nums[i] * digit;
        digit *= 10;
    }
    return answer;
}

// best
long long solution(long long n) {
    long long answer = 0;

    string str = to_string(n);
    sort(str.begin(), str.end(), greater<char>());
    answer = stoll(str);

    return answer;
}