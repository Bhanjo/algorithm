#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> ans;
    vector<int> temp = arr;
    sort(arr.begin(), arr.end());
    int target = arr[0];

    if (arr.size() == 1)
        ans.push_back(-1);
    else {
        for (int i = 0; i < temp.size(); i++) {
            if (target != temp[i])
                ans.push_back(temp[i]);
        }
    }

    return ans;
}

// best code
vector<int> solution(vector<int> arr) {
    if (arr.size() == 1) {
        return { -1 };
    }
    arr.erase(std::min_element(arr.begin(), arr.end()));
    return arr;
}