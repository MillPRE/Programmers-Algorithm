// https://school.programmers.co.kr/learn/courses/30/lessons/181924

function solution(arr, queries) {
    queries.forEach((q) => {
        const [i, j] = q;
        let tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    });

    return arr;
}
