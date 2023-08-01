// https://school.programmers.co.kr/learn/courses/30/lessons/181894

function solution(arr) {
    var answer = [];

    let first = arr.indexOf(2);
    let last = arr.lastIndexOf(2);

    if(first === -1) {
        return [-1];
    } else if(first === last) {
        return [2];
    } else {
        return arr.slice(first, last+1)
    }

    return answer;
}
