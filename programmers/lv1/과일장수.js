function solution(k, m, score) {
  score.sort((a, b) => {
    return b - a;
  });

  let answer = 0;
  let subBox = [];

  for (let i = 0; i < Math.floor(score.length / m) * m; i++) {
    subBox.push(score[i]);
    if (subBox.length >= m) {
      const minValue = Math.min(...subBox);
      answer += minValue * m;
      subBox = [];
    }
  }
  return answer;
}
