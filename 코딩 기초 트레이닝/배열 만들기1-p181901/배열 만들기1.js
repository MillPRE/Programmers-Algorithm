// https://school.programmers.co.kr/learn/courses/30/lessons/181901

function solution(n, k) {
    var answer = [k];


    while(answer[answer.length-1] < n) {
        answer.push(answer[answer.length-1] + k);
    }

    return answer[answer.length-1] > n ? answer.slice(0, answer.length-1) : answer;
}
