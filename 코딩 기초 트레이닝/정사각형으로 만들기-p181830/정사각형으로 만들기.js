// https://school.programmers.co.kr/learn/courses/30/lessons/181830
function solution(arr) {
    if(arr.length > arr[0].length) {
        let add = arr.length - arr[0].length;

        for(let i = 0 ; i < arr.length ; i++) {
            let a = new Array(add).fill(0);
            arr[i].push(...a);
        }
        // 행 < 열
    } else if(arr.length < arr[0].length) {
        // 열 < 행
        let add = arr[0].length - arr.length;

        for(let i = 0; i < add ; i++ ) {
            let a = new Array(arr[0].length).fill(0);
            arr.push(a);
        }
    }

    return arr;
}
