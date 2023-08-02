// https://school.programmers.co.kr/learn/courses/30/lessons/181865

function solution(binomial) {
    binomial = binomial.trim().split(" ");
    const a = Number(binomial[0])
    const op = binomial[1]
    const b = Number(binomial[2])

    if(op === '+') return a + b;
    if(op === '-') return a - b;
    return a * b;
}
