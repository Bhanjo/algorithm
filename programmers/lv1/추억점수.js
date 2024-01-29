function solution(name, yearning, photo) {
  const map = new Map();
  var answer = [];

  for (let i = 0; i < name.length; i++) {
    map.set(name[i], yearning[i]);
  }

  photo.forEach((arr) => {
    let sum = 0;
    arr.forEach((person) => {
      const score = map.get(person);
      if (score > 0) sum += score;
    });
    answer.push(sum);
  });
  return answer;
}
