function solution(new_id) {
  /*
    '/g' 일치하는 것 모두 찾기
    '^' 아닌 것 찾기
    '\w' 영어 알파벳, 숫자, 언더바
    '[^문자]' 괄호 안 문자 제외한 모든 문자 찾기
    '^문자' 특정 문자로 시작하는 것 찾기
    '문자$' 특정 문자로 끝나는 것 찾기
    '|' OR
  */
  const answer = new_id
    .toLowerCase() // 1
    .replace(/[^\w-_.]/g, '') // 2: 영단어, -, _, . 이 아닌 모든 것을 ''으로 치환
    .replace(/\.+/g, '.') // 3: .이 한 개 이상인 모든 것을 .으로 치환
    .replace(/^\.|\.$/g, '') // 4: .으로 시작하거나 .으로 끝나는 모든 것을 ''으로 치환
    .replace(/^$/, 'a') // 5: 단어가 시작끝(공백) 이면 'a' 넣기
    .slice(0, 15) // 6: 15자 초과면 15자로 맞추기
    .replace(/\.$/, ''); // 6: 끝 . 제거
  const len = answer.length;

  // 길이가 3 이상이면 그대로, 이하면 마지막 문자를 3-len 만큼 반복해 붙이기
  return len > 2 ? answer : answer + answer.charAt(len - 1).repeat(3 - len);
}
