// https://school.programmers.co.kr/learn/courses/30/lessons/181853

function solution(num_list) {
    num_list = num_list.sort(function(a,b) {
        return Number(a) - Number(b);
    }).slice(0, 5);

    return num_list;
}
