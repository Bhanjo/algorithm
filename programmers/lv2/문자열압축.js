function solution(s) {
  let answer = 10 ** 10;
  let temp = "";
  let candidateAnswer = "";

  if (s.length === 1) return 1;

  for (let i = 0; i < parseInt(s.length / 2); i++) {
    wordCnt = 1;
    temp += s[i];
    let copyTemp = temp;
    for (let j = i + 1; j < s.length; j += i + 1) {
      nextTemp = s.slice(j, j + temp.length);
      if (temp === nextTemp) {
        wordCnt += 1;
      } else {
        if (wordCnt === 1) {
          candidateAnswer += temp;
        } else {
          candidateAnswer += String(wordCnt) + temp;
        }
        wordCnt = 1;
        temp = nextTemp;
      }
    }
    temp = copyTemp;
    candidateAnswer += wordCnt > 1 ? String(wordCnt) + nextTemp : nextTemp;
    answer = Math.min(answer, candidateAnswer.length);
    candidateAnswer = "";
  }

  return answer;
}
