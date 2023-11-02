// 내 풀이 O(n^2)
function solution(t, p) {
  var answer = 0;
  let isBreak = false;
  let index = 0;

  while (true) {
    const stack = [];
    for (let i = index; i < index + p.length; i++) {
      if (i >= t.length) {
        isBreak = true;
        break;
      }
      stack.push(t[i]);
    }
    if (stack.length === p.length && +stack.join('') <= p) {
      answer += 1;
    }
    index += 1;
    if (isBreak) break;
  }

  return answer;
}

// 좋은 풀이 O(n)
function solution(t, p) {
  let count = 0;
  for (let i = 0; i <= t.length - p.length; i++) {
    let value = t.slice(i, i + p.length);
    if (+p >= +value) count++;
  }
  return count;
}
