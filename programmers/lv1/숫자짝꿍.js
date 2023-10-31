function solution(X, Y) {
  var answer = '';
  const tableX = new Array(10).fill(0);
  const tableY = new Array(10).fill(0);

  X.split('').map((item) => (tableX[+item] += 1));
  Y.split('').map((item) => (tableY[+item] += 1));

  for (let i = 9; i >= 0; i--) {
    if (tableX[i] > 0 && tableY[i]) {
      answer += `${i}`.repeat(Math.min(tableX[i], tableY[i]));
    }
  }

  if (answer === '') return '-1';
  if (+answer === 0) return '0';
  return answer;
}

solution('100', '2345');
