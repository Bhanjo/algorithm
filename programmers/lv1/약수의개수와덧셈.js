const gcdList = (num) => {
  let list = [];
  for (let i = 1; i <= parseInt(num ** (1 / 2)); i++) {
    if (num % i == 0) {
      let n = parseInt(num / i);
      list.push(i);
      if (i != n) list.push(n);
    }
  }
  return list;
};

function solution(left, right) {
  var answer = 0;

  for (let i = left; i <= right; i++) {
    const list = gcdList(i);
    if (list.length % 2 == 0) answer += i;
    else answer -= i;
  }
  return answer;
}
