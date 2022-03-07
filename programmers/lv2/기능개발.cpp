#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
  vector<int> answer;
  reverse(progresses.begin(), progresses.end());
  reverse(speeds.begin(), speeds.end());

  vector<int>doneTime;
  while (!progresses.empty() && !speeds.empty()) {
    int work = progresses[progresses.size() - 1];
    progresses.pop_back();
    int t = speeds[speeds.size() - 1];
    speeds.pop_back();

    // 제작 기간 구하기
    int restTime = 100 - work;
    int day = restTime / t;
    if (restTime % t > 0) day += 1;
    doneTime.push_back(day);
  }

  reverse(doneTime.begin(), doneTime.end());
  int workCnt = 0, maxTime = 0;
  bool isFirst = true;
  while (!doneTime.empty()) {
    int workTime = doneTime[doneTime.size() - 1];
    doneTime.pop_back();

    if (isFirst) {
      isFirst = false;
      maxTime = workTime;
    }
    else {
      if (workTime > maxTime) {
        maxTime = workTime;
        answer.push_back(workCnt);
        workCnt = 0;
      }
    }
    workCnt += 1;
  }
  if (workCnt) answer.push_back(workCnt);

  return answer;
}

// best
vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;

    int day;
    int max_day = 0;
    for (int i = 0; i < progresses.size(); ++i)
    {
        day = (99 - progresses[i]) / speeds[i] + 1;

        if (answer.empty() || max_day < day)
            answer.push_back(1);
        else
            ++answer.back();

        if (max_day < day)
            max_day = day;
    }

    return answer;
}