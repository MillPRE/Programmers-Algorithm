// https://school.programmers.co.kr/learn/courses/30/lessons/181911

function solution(my_strings, parts) {
    let answer = '';

    parts.forEach((p, index) => {
        answer += my_strings[index].slice(p[0], p[1]+1);
    });

    return answer;
}
