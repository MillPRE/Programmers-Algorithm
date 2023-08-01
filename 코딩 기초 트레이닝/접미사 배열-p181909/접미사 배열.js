// https://school.programmers.co.kr/learn/courses/30/lessons/181909

function solution(my_string) {
    var answer = [];

    my_string = my_string.split("").reverse().join('');

    for(let i = 1 ; i <= my_string.length ; i++) {
        answer.push(my_string.slice(0, i).split("").reverse().join(''));
    }

    answer.sort();

    return answer;
}
