// https://school.programmers.co.kr/learn/courses/30/lessons/181915

function solution(my_string, index_list) {
    var answer = '';

    my_string = my_string.split("");

    index_list.forEach((i) => {
        answer += my_string[i];
    });


    return answer;
}
