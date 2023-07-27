// https://school.programmers.co.kr/learn/courses/30/lessons/181903

function solution(q, r, code) {
    const answer = [];

    code.split("").forEach((c, index) => {
        if(index % q === r) {
            answer.push(c);
        }
    });
    return answer.join('');
}
