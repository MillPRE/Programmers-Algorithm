// https://school.programmers.co.kr/learn/courses/30/lessons/181880

function solution(num_list) {
    var answer = 0;

    num_list.forEach((num) => {
        while(num != 1) {
            if(num % 2 === 0) {
                answer += 1;
                num = num / 2;
            } else {
                num -= 1;
            }
        }
    })
    return answer;
}
