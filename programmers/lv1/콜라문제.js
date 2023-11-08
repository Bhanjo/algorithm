function solution(a, b, n) {
  var answer = 0;
  let rest = 0;

  while (n >= a) {
    const exchange = Math.floor(n / a) * b;
    rest += n % a;
    n = exchange;
    answer += exchange;
    if (n < a) {
      n += rest;
      rest = 0;
    }
  }
  return answer;
}

// 좋은 풀이
function solution(a, b, n) {
  let answer = 0;
  while (n >= a) {
    answer += parseInt(n / a) * b;
    n = parseInt(n / a) * b + (n % a);
  }
  return answer;
}
