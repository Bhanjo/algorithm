function solution(id_list, report, k) {
  let answer = {};
  let singo = {}; // 신고당한 횟수
  let users = {}; // 해당 유저가 신고한 사람들 리스트

  // 딕셔너리 초기화
  for (item of id_list) {
    answer[item] = 0;
    singo[item] = 0;
    users[item] = [];
  }

  // 신고하기, 동일한 사람은 동일한 사람을 한 번만 신고 가능
  for (item of report) {
    const arr = item.split(" ");
    // 아직 신고 안했을 때만 넣기
    if (!users[arr[0]].includes(arr[1])) {
      singo[arr[1]] += 1;
      users[arr[0]].push(arr[1]);
    }
  }

  // 신고 결과 전송하기
  for (key in singo) {
    // 신고를 k번 이상 당했으면 벤 결과 신고한 사람들에게 전송하기
    if (singo[key] >= k) {
      for (keyUser in users) {
        if (users[keyUser].includes(key)) {
          answer[keyUser] += 1;
        }
      }
    }
  }

  return Object.values(answer);
}
