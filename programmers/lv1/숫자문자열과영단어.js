function solution(s) {
  let arr = s.split("");
  var answer = "";
  let temp = [];
  let comp = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
  ];

  while (arr.length > 0) {
    let a = arr.shift();
    // 숫자면 바로 답 삽입
    if (0 <= parseInt(a) && parseInt(a) <= 9) {
      answer += a;
    } else {
      temp.push(a);
      const alpha = temp.join("");
      const idx = comp.indexOf(alpha);
      if (idx != -1) {
        temp = [];
        console.log(idx, alpha);
        answer += String(idx);
      }
    }
  }
  return parseInt(answer);
}

// 다른 풀이
function solution(s) {
  let numbers = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
  ];
  var answer = s;

  for (let i = 0; i < numbers.length; i++) {
    // one, two 와 같은 문자열 기준으로 나누기
    let arr = answer.split(numbers[i]);
    // numbers[i]로 나눠진 배열에 숫자 i를 중간중간 넣어 합치기
    answer = arr.join(i);
  }

  return Number(answer);
}

solution("one4seveneight");
