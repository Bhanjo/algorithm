#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    bool* arr = new bool[n + 1];
    for (int i = 2; i <= n; i++)
        arr[i] = true;

    for (int i = 2; i * i <= n; i++) {
        if (arr[i]) {
            for (int j = i * i; j <= n; j += i) {
                arr[j] = false;
            }
        }
    }

    for (int i = 2; i <= n; i++) {
        if (arr[i])
            answer += 1;
    }
    return answer;
}

// best
int solution(int n) {
    int answer = 0;
    vector<bool> tmp(n + 1, true);

    for (int i = 2; i < n + 1; i++) {
        if (tmp[i] == true) {
            for (int j = 2; i * j < n + 1; j++) tmp[i * j] = false;
            answer++;
        }
    }

    return answer;
}