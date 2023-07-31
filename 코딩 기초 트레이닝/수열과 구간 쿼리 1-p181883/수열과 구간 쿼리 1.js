// https://school.programmers.co.kr/learn/courses/30/lessons/181883

function solution(arr, queries) {
    // s <= i <- e 라면 arr[i] + 1
    const answer = [...arr];

    queries.forEach((q, index) => {
        arr.forEach((a, i) => {
            if(i >= q[0] && i <= q[1]) {
                answer[i] += 1;
            }
        });
    });


    return answer;
}
