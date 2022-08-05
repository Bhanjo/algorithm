function solution(answers) {
  let answer = [];
  let p1 = [1, 2, 3, 4, 5];
  let p2 = [2, 1, 2, 3, 2, 4, 2, 5];
  let p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
  let pCnt = [0, 0, 0];

  for (i in answers) {
    if (p1[i % 5] == answers[i]) pCnt[0] += 1;
    if (p2[i % 8] == answers[i]) pCnt[1] += 1;
    if (p3[i % 10] == answers[i]) pCnt[2] += 1;
  }

  const top = Math.max(...pCnt);
  for (let i = 0; i < 3; i++) {
    if (top === pCnt[i]) answer.push(i + 1);
  }

  return answer;
}
