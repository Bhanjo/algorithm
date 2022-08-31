function solution(sizes) {
  let ans1 = -(10 ** 10);
  let ans2 = -(10 ** 10);
  for (let i of sizes) {
    let maxVal = i[0] > i[1] ? i[0] : i[1];
    let minVal = i[0] > i[1] ? i[1] : i[0];
    ans1 = ans1 < maxVal ? maxVal : ans1;
    ans2 = ans2 < minVal ? minVal : ans2;
  }
  return ans1 * ans2;
}
