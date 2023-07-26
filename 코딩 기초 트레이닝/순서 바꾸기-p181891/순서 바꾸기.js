// https://school.programmers.co.kr/learn/courses/30/lessons/181891

function solution(num_list, n) {
    var answer = [];
    const left = num_list.slice(0, n);
    const right = num_list.slice(n, num_list.length);

    return [...right, ...left];
}
