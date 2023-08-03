// https://school.programmers.co.kr/learn/courses/30/lessons/181859


function solution(arr) {
    const answer = [];
    let i = 0;

    while(i < arr.length) {
        if(answer.length === 0) {
            answer.push(arr[i]);
            i += 1;
        } else if(answer.length > 0 && answer[answer.length -1] === arr[i]) {
            answer.pop();
            i += 1;
        } else if(answer.length > 0 && answer[answer.length -1] !== arr[i]) {
            answer.push(arr[i]);
            i += 1;
        }
    }

    return answer.length > 0 ? answer : [-1];
}
