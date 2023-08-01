// https://school.programmers.co.kr/learn/courses/30/lessons/181885

function solution(todo_list, finished) {
    var answer = [];

    todo_list.forEach((t, index) => {
        if(!finished[index]) answer.push(t);
    });

    return answer;
}
