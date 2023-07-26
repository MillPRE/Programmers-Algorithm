// https://school.programmers.co.kr/learn/courses/30/lessons/181884

function solution(numbers, n) {
    var answer = 0;

    for(let i = 0; i < numbers.length ;i++) {
        answer += numbers[i];
        if(answer > n) break;
    }

    return answer;
}
