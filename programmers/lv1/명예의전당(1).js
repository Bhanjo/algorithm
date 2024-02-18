function solution(k, score) {
  let answer = [];
  let stack = [];
  let minValue = 0;
  score.forEach((value) => {
    if (stack.length < k) {
      stack.push(value);
    } else if (stack[0] <= value) {
      stack = stack.slice(1, stack.length);
      stack.push(value);
    }
    stack.sort((a, b) => a - b);
    minValue = stack[0];
    answer.push(stack[0]);
  });
  return answer;
}
