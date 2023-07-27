// https://school.programmers.co.kr/learn/courses/30/lessons/181870

function solution(strArr) {
    const answer = [];

    strArr.forEach((s) => {
        if(s.indexOf('ad') < 0) {
            answer.push(s);
        }
    });


    return answer;
}
