// https://school.programmers.co.kr/learn/courses/30/lessons/181902

function solution(my_string) {
    // # 0 ~ 25: A ~ Z
    // # 26 ~ 52: a ~ z
    // # A ~ Z: 65 ~ 90
    // # a ~ z: 97 ~ 122
    const answer = new Array(52).fill(0);

    my_string.split('').forEach((s) => {
        if(s.charCodeAt() <= 90) {
            answer[s.charCodeAt() % 65] += 1;
        } else {
            answer[s.charCodeAt() % 97 + 26] += 1;
        }
    });


    return answer;
}
