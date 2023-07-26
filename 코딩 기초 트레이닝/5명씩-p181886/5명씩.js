// https://school.programmers.co.kr/learn/courses/30/lessons/181886

function solution(names) {
    var answer = [];

    let temp = [];
    for(let i = 0 ; i < names.length ; i++) {
        temp.push(names[i]);

        if(temp.length === 5) {
            answer.push(temp[0]);
            temp = [];
        }
    }

    return temp.length === 0 ? answer : [...answer, temp[0]];
}
