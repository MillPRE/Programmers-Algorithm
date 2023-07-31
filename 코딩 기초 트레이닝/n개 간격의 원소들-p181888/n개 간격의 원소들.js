// https://school.programmers.co.kr/learn/courses/30/lessons/181888

function solution(num_list, n) {
    var answer = [];
    let cnt = 0;

    num_list.forEach((num, index) => {
        if (cnt === 0) {
            answer.push(num);
            cnt = n -1;
        } else {
            cnt -= 1;
        }
    });

    return answer;
}
