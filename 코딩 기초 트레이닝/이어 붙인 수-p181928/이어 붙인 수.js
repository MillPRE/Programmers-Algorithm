// https://school.programmers.co.kr/learn/courses/30/lessons/181928

function solution(num_list) {
    var answer = 0;
    let odd = '';
    let even = '';

    num_list.forEach((n) => {
        if(n % 2 === 0) {
            even += n
        } else {
            odd += n
        }
    })


    return Number(even) + Number(odd);
}
