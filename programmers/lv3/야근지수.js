function solution(n, works) {
  let answer = 0;

  works.sort((a, b) => b - a);
  let maxValue = works[0];

  while (n > 0) {
    for (let i = 0; i < works.length; i++) {
      if (maxValue === works[i]) {
        works[i] = works[i] > 0 ? works[i] - 1 : 0;
        n -= 1;
      }
      if (n <= 0) break;
    }
    maxValue -= 1;
    if (maxValue <= 0) break;
  }

  works.map((item) => (answer += item ** 2));

  return answer;
}
