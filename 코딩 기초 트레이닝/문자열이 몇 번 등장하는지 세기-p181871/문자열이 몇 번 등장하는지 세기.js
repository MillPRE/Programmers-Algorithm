// https://school.programmers.co.kr/learn/courses/30/lessons/181871

function solution(myString, pat) {
    var answer = 0;

    for(let i = 0; i <= myString.length - pat.length ; i++) {
        if(myString.slice(i, i+pat.length) === pat) {
            answer += 1;
        }
    }

    return answer;
}
