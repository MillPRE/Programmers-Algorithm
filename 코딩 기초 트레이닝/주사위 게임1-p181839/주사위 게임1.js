// https://school.programmers.co.kr/learn/courses/30/lessons/181839

function solution(a, b) {
    // a and b odd -> a^2 + b^2
    // a or b odd
    // -> 2 * (a + b)
    // a and b even -> | a - b |
    if( a % 2 !== 0 && b % 2 !== 0 ) {
        return a**2 + b **2;
    } else if( a % 2 === 0 && b % 2 ===0) {
        return Math.abs(a-b);
    } else {
        return 2 * (a+b);
    }
}
