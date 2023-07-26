function solution(arr, n) {
    var answer = [];

    arr.forEach((d, index) => {
        if(arr.length % 2 === 0) {
            // arr 길이 짝수
            answer.push(d + (index % 2 === 0 ? 0 : n));
        } else {
            // arr 길이 홀수
            answer.push(d + (index % 2 !== 0 ? 0 : n));
        }
    });

    return answer;
}
