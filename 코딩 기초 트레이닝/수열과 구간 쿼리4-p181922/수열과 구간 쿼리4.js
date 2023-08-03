// https://school.programmers.co.kr/learn/courses/30/lessons/181922

function solution(arr, queries) {
    const answer = [];

    queries.forEach((q) => {
        const s = q[0];
        const e = q[1];
        const k = q[2];

        arr = arr.map((a, index) => {
            if(index >= s && index <= e && index % k === 0 ) {
                return a +1;
            } else {
                return a;
            }
        });
    });

    return arr;
}
