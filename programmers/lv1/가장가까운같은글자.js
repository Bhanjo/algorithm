function solution(s) {
  var answer = [];
  const strMap = new Map();
  s.split('').forEach((str, index) => {
    strMap.has(str) ? answer.push(index - strMap.get(str)) : answer.push(-1);
    strMap.set(str, index);
  });
  return answer;
}
