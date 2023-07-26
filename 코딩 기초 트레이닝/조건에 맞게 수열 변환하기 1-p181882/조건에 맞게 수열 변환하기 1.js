// https://school.programmers.co.kr/learn/courses/30/lessons/181882

function solution(arr) {
    var answer = [];
    // x < 50 && odd -> x * 2
    // x >= 50 & even -> x / 2

    arr.forEach((x) => {
        if(x < 50 && x % 2 !== 0) {
            answer.push(x * 2);
        } else if(x >= 50 && x % 2 === 0) {
            answer.push(x / 2);
        } else {
            answer.push(x);
        }
    });


    return answer;
}
