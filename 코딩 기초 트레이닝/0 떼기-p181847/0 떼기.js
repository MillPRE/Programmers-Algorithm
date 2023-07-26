// https://school.programmers.co.kr/learn/courses/30/lessons/181847

function solution(n_str) {
    n_str = n_str.split("");
    while(n_str[0] === '0') {
        n_str.shift();
    }

    return n_str.join('');
}
