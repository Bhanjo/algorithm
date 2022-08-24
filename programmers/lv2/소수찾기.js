function solution(numbers) {
  var answer = 0;
  let nums = [];
  let check = {};
  let temp = [];
  let visit = new Array(numbers.length).fill(false);

  for (let i = 0; i < numbers.length; i++) {
    nums.push(numbers[i]);
  }

  const isPrime = (n) => {
    if (n == 0 || n == 1) return false;
    if (n == 2) return true;
    for (let i = 2; i <= parseInt(n ** (1 / 2)); i++) {
      if (n % i == 0) return false;
    }
    return true;
  };

  const dfs = () => {
    let num = parseInt(temp.join(""));
    if (num && !(num in check)) {
      check[num] = true;
      if (isPrime(num)) answer += 1;
    }
    for (let i = 0; i < nums.length; i++) {
      if (!visit[i]) {
        visit[i] = true;
        temp.push(nums[i]);
        dfs();
        temp.pop();
        visit[i] = false;
      }
    }
  };

  dfs();
  return answer;
}
