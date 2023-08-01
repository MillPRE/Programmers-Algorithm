// https://school.programmers.co.kr/learn/courses/30/lessons/181852

function solution(num_list) {
    num_list.sort(function(a,b) {
        return Number(a) - Number(b);
    });

    num_list = num_list.slice(5, );

    return num_list;
}
