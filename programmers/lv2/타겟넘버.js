var len = 0;
var answer = 0;
var TARGET = 0;
var nums = [];

function dfs(index, hap) {
  if (index == len) {
    if (hap === TARGET) {
      answer += 1;
    }
    return;
  }
  dfs(index + 1, hap + nums[index]);
  dfs(index + 1, hap - nums[index]);
}

function solution(numbers, target) {
  len = numbers.length;
  TARGET = target;
  nums = numbers;
  dfs(0, 0);
  return answer;
}
