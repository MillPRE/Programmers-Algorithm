// https://school.programmers.co.kr/learn/courses/30/lessons/181905

function solution(my_string, s, e) {
    var answer = my_string.slice(0, s);
    let tmp = my_string.slice(s, e+1).split("").reverse().join('');
    answer += tmp;
    answer += my_string.slice(e+1, );
    return answer;
}
