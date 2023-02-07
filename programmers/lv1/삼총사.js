function solution(number) {
  let answer = 0;
  let visit = new Array(number.length).fill(false);

  const dfs = (idx, nums, arr) => {
    if (nums.length === 3) {
      if (nums.reduce((hap, curr) => hap + curr, 0) === 0) {
        answer += 1;
      }
      return;
    }

    for (let i = idx; i < arr.length; i++) {
      if (visit[i]) continue;

      nums.push(arr[i]);
      visit[i] = true;
      dfs(i, nums, arr);
      visit[i] = false;
      nums.pop();
    }
  };

  dfs(0, [], number);
  return answer;
}
