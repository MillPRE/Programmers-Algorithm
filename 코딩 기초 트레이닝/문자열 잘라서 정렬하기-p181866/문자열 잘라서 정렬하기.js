// https://school.programmers.co.kr/learn/courses/30/lessons/181866

function solution(myString) {
    var answer = [];

    let current = '';
    myString = myString.split("");
    myString.forEach((d, index) => {
        if(d === 'x') {
            if(current.length !== 0) {
                answer.push(current);
                current = '';
            }
        } else {
            current += d;
        }
    });

    if(current.length > 0) answer.push(current);
    answer.sort();

    return answer;
}
