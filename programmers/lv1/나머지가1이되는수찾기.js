function solution(n) {
  var answer = 2;
  while (true) {
    if (n % answer == 1) {
      break;
    }
    answer += 1;
  }
  return answer;
}
