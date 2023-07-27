// https://school.programmers.co.kr/learn/courses/30/lessons/181912

function solution(intStrs, k, s, l) {
    const answer = [];

    intStrs.forEach((i) => {
        i = i.slice(s, s+l);
        if(Number(i) > k) answer.push(Number(i));
    });

    return answer;
}
