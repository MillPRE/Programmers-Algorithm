// https://school.programmers.co.kr/learn/courses/30/lessons/12980

function solution(n) {
    let ans = 0;

    while(n > 0) {
        if ( n % 2 !== 0) {
            n -= 1;
            ans ++;
        } else {
            n = n / 2;
        }
    }

    return ans;
}