function solution(board, moves) {
  var answer = 0;
  let st = [];

  for (let i of moves) {
    let pick = i - 1;
    // 크래인으로 집어서 st에 넣기
    for (let y = 0; y < board.length; y++) {
      if (board[y][pick] > 0) {
        st.push(board[y][pick]);
        board[y][pick] = 0;
        break;
      }
    }
    if (st.length >= 2) {
      top1 = st.pop();
      top2 = st.pop();
      if (top1 == top2) {
        answer += 2;
      } else {
        st.push(top2);
        st.push(top1);
      }
    }
  }
  return answer;
}
