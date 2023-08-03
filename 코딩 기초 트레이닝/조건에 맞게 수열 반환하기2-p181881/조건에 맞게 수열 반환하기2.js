// https://school.programmers.co.kr/learn/courses/30/lessons/181881
function solution(arr) {
    let answer = 0;
    let prev = [];
    let current = arr;

    const transform = (arr) => {
        arr = arr.map((a) => {
            if(a >= 50 && a % 2 === 0) {
                return a / 2;
            } else if (a <= 50 && a % 2 !== 0) {
                return a * 2 + 1;
            } else {
                return a;
            }
        });

        return arr;
    }

    while(prev.join('') !== current.join('')) {
        prev = current;
        current = transform(prev);
        answer += 1;
    }


    return answer -1;
}
