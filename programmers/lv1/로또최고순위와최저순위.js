function solution(lottos, win_nums) {
  var answer = [];
  let cntZero = 0;
  let cnt = 0;
  let rank = [6, 6, 5, 4, 3, 2, 1];

  lottos = lottos.sort((a, b) => a - b);
  win_nums = win_nums.sort((a, b) => a - b);

  for (let i = 0; i < 6; i++) {
    if (lottos[i] == 0) {
      cntZero += 1;
      continue;
    }
    for (let j = 0; j < 6; j++) {
      if (lottos[i] == win_nums[j]) cnt += 1;
    }
  }

  answer.push(rank[cnt + cntZero], rank[cnt]);
  return answer;
}

// 다른 풀이
function solution(lottos, win_nums) {
  var answer = [];
  let rank = [6, 6, 5, 4, 3, 2, 1];

  const cnt = lottos.filter((i) => win_nums.includes(i)).length;
  const cntZero = lottos.filter((i) => i === 0).length;

  answer.push(rank[cnt + cntZero], rank[cnt]);
  return answer;
}
