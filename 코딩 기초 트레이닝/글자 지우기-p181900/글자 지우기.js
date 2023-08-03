// https://school.programmers.co.kr/learn/courses/30/lessons/181900

function solution(my_string, indices) {
    var answer = '';
    my_string = my_string.split("");
    my_string.forEach((m, index) => {
        if(!indices.includes(index)) {
            answer += m;
        }
    });

    return answer;
}
