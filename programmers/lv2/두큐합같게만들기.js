function solution(queue1, queue2) {
  var answer = -1;
  const sum = (arr) => arr.reduce((a, b) => a + b);

  let sumA = sum(queue1);
  let sumB = sum(queue2);
  let target = (sumA + sumB) / 2;
  let left = 0,
    right = queue1.length;

  let list = [...queue1, ...queue2];
  let limit = list.length * 3;

  let cnt = 0;
  while (cnt <= limit) {
    if (sumA == target) {
      answer = cnt;
      break;
    } else if (sumA > target) {
      sumA -= list[left];
      left += 1;
    } else {
      sumA += list[right];
      right += 1;
    }
    cnt += 1;
  }

  return answer;
}
