function solution(cards1, cards2, goal) {
  let flag = true;
  while (goal.length > 0) {
    if (cards1.length > 0 && cards1[0] === goal[0]) {
      cards1.shift();
      goal.shift();
    } else if (cards2.length > 0 && cards2[0] === goal[0]) {
      cards2.shift();
      goal.shift();
    } else {
      flag = false;
      break;
    }
  }

  return flag ? 'Yes' : 'No';
}

// 다른 풀이
function solution(cards1, cards2, goal) {
  for (const s of goal) {
    if (cards1[0] == s) {
      cards1.shift();
    } else if (cards2[0] == s) {
      cards2.shift();
    } else {
      return 'No';
    }
  }

  return 'Yes';
}
