function solution(arr) {
    let answer = 0;
    arr.forEach((num) => {
        answer += num;
    });
    answer /= arr.length
    return answer;
}