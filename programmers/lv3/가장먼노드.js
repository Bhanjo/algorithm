function solution(n, edge) {
  // 그래프 초기화
  let graph = new Array(n + 1).fill(null).map(() => new Array());

  // 간선 추가
  for (let i of edge) {
    let from = i[0],
      to = i[1];
    graph[from].push(to);
    graph[to].push(from);
  }

  const bfs = () => {
    let q = [];
    visit = new Array(n + 1).fill(0);
    visit[1] = 1;

    q.push(1);
    while (q.length > 0) {
      let node = q.shift();
      for (let next of graph[node]) {
        if (!visit[next]) {
          visit[next] = visit[node] + 1;
          q.push(next);
        }
      }
    }
  };

  bfs();
  maxVal = Math.max(...visit);
  let count = visit.reduce((cnt, check) => cnt + (check == maxVal), 0);

  return count;
}
