// https://school.programmers.co.kr/learn/courses/30/lessons/181856

function solution(arr1, arr2) {
    if(arr1.length === arr2.length) {
        let re1 = arr1.reduce((a, b) => a + b, 0);
        let re2 = arr2.reduce((a, b) => a + b, 0);

        if(re1 === re2) {
            return 0;
        } else {
            return re1 > re2 ? 1 : -1;
        }
    } else {
        return arr1.length > arr2.length ? 1 : -1
    }

    return answer;
}
