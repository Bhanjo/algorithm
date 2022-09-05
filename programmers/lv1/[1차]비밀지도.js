function bin(num, n) {
  let list = [];
  while (num) {
    list.push(num % 2);
    num = parseInt(num / 2);
  }
  while (list.length < n) {
    list.push(0);
  }
  return list.reverse();
}

function solution(n, arr1, arr2) {
  var answer = [];
  let graph1 = [],
    graph2 = [];

  for (let i = 0; i < arr1.length; i++) {
    const b1 = bin(arr1[i], n);
    const b2 = bin(arr2[i], n);
    graph1.push(b1);
    graph2.push(b2);
  }

  for (let i = 0; i < n; i++) {
    row = "";
    for (let j = 0; j < n; j++) {
      if (graph1[i][j] == 1 || graph2[i][j] == 1) {
        row += "#";
      } else if (graph1[i][j] == 0 || graph2[i][j] == 0) {
        row += " ";
      }
    }
    answer.push(row);
  }

  return answer;
}
