function solution(N, stages) {
  var answer = [];
  let dir = [];
  for (let i = 1; i <= N; i++) {
    let notClear = 0;
    let goal = 0;
    for (let stage of stages) {
      if (i == stage) {
        notClear += 1;
        goal += 1;
      }
      if (i < stage) goal += 1;
    }
    dir.push([i, notClear / goal]);
  }
  dir.sort((a, b) => {
    return b[1] - a[1];
  });

  for (let i of dir) {
    answer.push(i[0]);
  }
  return answer;
}
