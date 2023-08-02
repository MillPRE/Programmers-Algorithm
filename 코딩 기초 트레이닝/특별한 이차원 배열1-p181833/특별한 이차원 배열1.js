// https://school.programmers.co.kr/learn/courses/30/lessons/181833

function solution(n) {
    const answer = Array.from(Array(n), () => Array(n).fill(0));

    for(let i = 0 ; i < n ; i++) {
        answer[i][i] = 1;
    }
    return answer;
}
