// https://school.programmers.co.kr/learn/courses/30/lessons/181858

function solution(arr, k) {
    const answer = [];
    let i = 0;
    while(answer.length < k) {
        if(!answer.includes(arr[i])) {
            answer.push(arr[i]);
        }
        i++;

        if(i === arr.length && answer.length < k) {
            break;
        }
    }

    if(answer.length < k) {
        while(answer.length < k) {
            answer.push(-1);
        }
    }

    return answer;
}
