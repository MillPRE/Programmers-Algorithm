// https://school.programmers.co.kr/learn/courses/30/lessons/181873

function solution(my_string, alp) {
    my_string = my_string.split('').map((s) => {
        if(s === alp) {
            return alp.toUpperCase();
        } else {
            return s;
        }
    });

    return my_string.join('');
}
