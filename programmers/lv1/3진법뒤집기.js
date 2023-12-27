function solution(n) {
  var answer = [];

  while (n > 0) {
    answer.unshift(n % 3);
    n = Math.floor(n / 3);
  }

  const hap = answer.reduce(
    (prev, value, idx) => prev + value * Math.pow(3, idx),
    0
  );
  return hap;
}
