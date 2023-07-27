// https://school.programmers.co.kr/learn/courses/30/lessons/181844

function solution(arr, delete_list) {
    var answer = [];

    arr.forEach((a) => {
        if(!delete_list.includes(a)) {
            return answer.push(a);
        }
    });


    return answer;
}
