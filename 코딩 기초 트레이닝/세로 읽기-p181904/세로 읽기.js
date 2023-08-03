// https://school.programmers.co.kr/learn/courses/30/lessons/181904

function solution(my_string, m, c) {
    var answer = '';
    my_string = my_string.split("");

    let cnt = 0;

    my_string.forEach((d) => {
        cnt += 1;
        if(cnt === c) {
            answer += d
        };

        if(cnt === m) {
            cnt = 0;
        }
    });

    return answer;
}
