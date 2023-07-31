// https://school.programmers.co.kr/learn/courses/30/lessons/181887

function solution(num_list) {
    var answer = [0,0];
    // answer[0] 홀수
    // answer[1] 짝수
    num_list.forEach((n, index) => {
        if((index + 1) % 2 === 0) {
            answer[1] += n;
        } else {
            answer[0] += n;
        }
    });

    return answer[0] >= answer[1] ? answer[0] : answer[1];
}
