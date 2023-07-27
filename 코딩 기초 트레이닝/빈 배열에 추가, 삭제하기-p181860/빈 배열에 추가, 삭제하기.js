// https://school.programmers.co.kr/learn/courses/30/lessons/181860

function solution(arr, flag) {
    let X = [];

    flag.forEach((f, index) => {
        if(f) {
            const a = new Array(arr[index] * 2).fill(arr[index]);

            X = X.concat(...a);
        } else {
            X = X.slice(0, X.length-arr[index]);
        }
    });

    return X;
}
