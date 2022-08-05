function solution(maps) {
  let answer = -1;
  let dx = [-1, 1, 0, 0];
  let dy = [0, 0, -1, 1];
  let q = [];

  let visit = [];
  for (let i = 0; i < maps.length; i++) {
    let row = [];
    for (let j = 0; j < maps[i].length; j++) {
      row.push(0);
    }
    visit.push(row);
  }

  q.push([0, 0]);
  visit[0][0] = 1;

  while (q.length > 0) {
    let pos = q.shift();
    // console.log('방문', pos);
    if (pos[0] === maps.length - 1 && pos[1] === maps[0].length - 1) {
      answer = visit[visit.length - 1][visit[0].length - 1];
    }
    for (let i = 0; i < 4; i++) {
      let mx = pos[0] + dx[i];
      let my = pos[1] + dy[i];
      if (0 <= mx && mx < maps.length && 0 <= my && my < maps[0].length) {
        if (maps[mx][my] === 1 && visit[mx][my] === 0) {
          visit[mx][my] = visit[pos[0]][pos[1]] + 1;
          q.push([mx, my]);
        }
      }
    }
  }
  return answer;
}
