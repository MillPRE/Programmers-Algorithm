// https://school.programmers.co.kr/learn/courses/30/lessons/181875

function solution(strArr) {
    var answer = [];

    strArr.forEach((s, index) => {
        if(index % 2 === 0) {
            answer.push(s.toLowerCase());
        } else {
            answer.push(s.toUpperCase());
        }
    });

    return answer;
}
