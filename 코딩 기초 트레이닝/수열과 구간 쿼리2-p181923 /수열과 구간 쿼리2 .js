// https://school.programmers.co.kr/learn/courses/30/lessons/181923

function solution(arr, queries) {
    var answer = [];

    queries.forEach((q) => {
        let s = q[0];
        let e = q[1];
        let k = q[2];

        let tmp = arr.slice(s, e+1);
        tmp = tmp.filter(t => t > k);
        tmp.sort(function(a,b) {
            return Number(a) - Number(b);
        });

        if(tmp.length > 0) answer.push(tmp[0]);
        else answer.push(-1);
    });

    return answer;
}
