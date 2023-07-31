// https://school.programmers.co.kr/learn/courses/30/lessons/181857

function solution(arr) {

    if(arr.length & arr.length -1 === 0) {
        return arr;
    }

    while((arr.length & arr.length -1 )!== 0) {
        arr.push(0);
    }

    return arr;
}
