// https://school.programmers.co.kr/learn/courses/30/lessons/181926

function solution(n, control) {
    const dic = {
        'w': 1,
        's': -1,
        'd': 10,
        'a': -10
    };

    let answer = n;
    control = control.split("");

    control.forEach((c) => {
        answer += dic[c];
    });

    return answer;
}
