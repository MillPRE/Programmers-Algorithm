// https://school.programmers.co.kr/learn/courses/30/lessons/181931

function solution(a, d, included) {
    let answer = 0;
    let current = 0;

    included.forEach((value, index) => {
        current += index === 0 ? a : d;
        answer += value ? current : 0;
    });

    return answer;
}
