function solution(array, commands) {
  let answer = [];
  for (let i = 0; i < commands.length; i++) {
    let start = commands[i][0];
    let end = commands[i][1];
    let idx = commands[i][2];
    let arr = array.slice(start - 1, end);
    arr.sort((a, b) => {
      return a - b;
    });
    answer.push(arr[idx - 1]);
  }
  return answer;
}
