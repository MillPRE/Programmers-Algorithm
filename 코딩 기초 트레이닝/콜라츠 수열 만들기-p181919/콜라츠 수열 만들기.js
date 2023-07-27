// https://school.programmers.co.kr/learn/courses/30/lessons/181919

function solution(n) {
    var answer = [n];

    let current = n;

    while(current > 1) {
        if(current % 2 === 0) {
            // 짝수
            current = current / 2;
        } else {
            // 홀수
            current = current * 3 + 1;
        }
        answer.push(current);
    }
    return answer;
}
