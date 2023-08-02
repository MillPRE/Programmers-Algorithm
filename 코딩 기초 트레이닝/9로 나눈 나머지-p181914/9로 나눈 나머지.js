// https://school.programmers.co.kr/learn/courses/30/lessons/181914

function solution(number) {
    number = BigInt(number)
    return Number(number % 9n);
}
