// https://school.programmers.co.kr/learn/courses/30/lessons/181908

function solution(my_string, is_suffix) {
    if(my_string.indexOf(is_suffix) < 0) {
        return 0;
    } else {
        if(my_string.lastIndexOf(is_suffix) === my_string.length - is_suffix.length) {
            return 1;
        } else {
            return 0;
        }
    }
}
