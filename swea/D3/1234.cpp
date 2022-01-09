#include<iostream>
#include <stack>
#include <string>
using namespace std;

int main() {
    for (int tc = 1; tc <= 10; tc++) {
        int n;
        string pwd;
        stack<char> st, outSt;
        cin >> n >> pwd;

        for (int i = 0; i < n; i++) {
            // push 조건
            if(st.empty() || st.top() != pwd[i])
                st.push(pwd[i]);
            else if(st.top() == pwd[i]) { // pop 조건
                st.pop();
            }
        }

        while(!st.empty()) {
            outSt.push(st.top());
            st.pop();
        }

        cout << "#" << tc << " ";
        while (!outSt.empty()) {
            cout << outSt.top();
            outSt.pop();
        }
        cout << "\n";
    }
    return 0;
}
