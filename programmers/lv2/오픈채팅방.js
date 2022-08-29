function solution(record) {
  var answer = [];
  let users = {};
  let temp = [];

  for (let i of record) {
    let info = i.split(" ");
    // 유저의 닉네임 갱신
    if (info.length === 3) users[info[1]] = info[2];

    if (info[0] === "Change") continue;

    let msg = "";
    if (info[0] == "Enter") msg = [info[1], "님이 들어왔습니다."];
    else if (info[0] == "Leave") msg = [info[1], "님이 나갔습니다."];
    temp.push(msg);
  }

  for (let arr of temp) {
    let msg = users[arr[0]] + arr[1];
    answer.push(msg);
  }

  return answer;
}
