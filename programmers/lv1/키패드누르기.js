function solution(numbers, hand) {
  var answer = "";
  // 0~9 까지
  let pad = [
    [3, 1],
    [0, 0],
    [0, 1],
    [0, 2],
    [1, 0],
    [1, 1],
    [1, 2],
    [2, 0],
    [2, 1],
    [2, 2],
  ];
  // 왼손 = *, 오른손 = #
  let posL = [3, 0];
  let posR = [3, 2];

  for (let i of numbers) {
    if (i == 1 || i == 4 || i == 7) {
      answer += "L";
      posL = pad[i];
    }
    if (i == 3 || i == 6 || i == 9) {
      answer += "R";
      posR = pad[i];
    }
    if (i == 2 || i == 5 || i == 8 || i == 0) {
      // 거리 파악
      let distL = Math.abs(posL[0] - pad[i][0]) + Math.abs(posL[1] - pad[i][1]);
      let distR = Math.abs(posR[0] - pad[i][0]) + Math.abs(posR[1] - pad[i][1]);
      // 두 값이 같으면 주 사용 손에 따라 다름
      if (distL == distR) {
        answer += hand == "right" ? "R" : "L";
        if (hand == "right") posR = pad[i];
        else posL = pad[i];
      } else if (distL < distR) {
        answer += "L";
        posL = pad[i];
      } else {
        answer += "R";
        posR = pad[i];
      }
    }
  }
  return answer;
}
