// https://school.programmers.co.kr/learn/courses/30/lessons/181893

function solution(arr, query) {
    query.forEach((q, index) => {
        if(index % 2 === 0) {
            arr = arr.filter((a, i) => {
                return i <= q;
            });
        } else {
            arr = arr.filter((a, i) => {
                return i >= q;
            })
        }
    })

    return arr;
}
