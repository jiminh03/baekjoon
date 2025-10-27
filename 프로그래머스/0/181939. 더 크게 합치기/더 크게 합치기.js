function solution(a, b) {
    var answer = '';
    let answer1 = '';
    answer = Number(String(a) + String(b))
    answer1 = Number(String(b) + String(a))
    return answer >= answer1 ? answer : answer1;
}