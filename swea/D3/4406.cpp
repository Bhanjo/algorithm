#include <iostream>
#include <string>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;
    string word;
    getline(cin, word);
    for (int tc = 1; tc <= n; tc++) {
        getline(cin, word);
        int len = word.length();
        int i = 0;
        while (i < word.length()) {
            if(word[i] == 'a' || word[i] == 'e' || word[i] == 'i' || word[i] == 'o' || word[i] == 'u')
                word.erase(i, 1);
            else
                i += 1;
        }
        cout << "#" << tc << " " << word << "\n";
    }
}
