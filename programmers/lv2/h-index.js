function solution(citations) {
  var answer = 0;
  let maxValue = Math.max(...citations);

  for (let h = maxValue; h > -1; h--) {
    let cnt = 0;
    for (let i of citations) if (i >= h) cnt += 1;
    if (cnt >= h) answer = Math.max(answer, h);
  }

  return answer;
}
