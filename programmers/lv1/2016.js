function solution(a, b) {
    let answer = '';
    let month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    let date = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    let num = 0
    for(let i = 1; i < a; i++) {
        num += month[i-1]
    }
    num += b
    answer = date[num % 7]
    return answer
}