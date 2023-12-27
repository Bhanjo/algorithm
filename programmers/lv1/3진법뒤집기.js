function solution(n) {
  var answer = [];

  while (n > 1) {
    answer.push(n % 3);
    n = Math.floor(n / 3);
    console.log(n);
  }

  if (n > 0) answer.push(n);

  let cnt = 1;
  let hap = 0;
  while (answer.length > 0) {
    hap += cnt * answer.pop();
    cnt *= 3;
  }
  return hap;
}
