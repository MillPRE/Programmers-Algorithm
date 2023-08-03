// https://school.programmers.co.kr/learn/courses/30/lessons/181837

function solution(order) {
    // 아메리카노: 4500
    // 카페라떼: 5000
    // 아무거나 : 4500
    let answer = 0;

    order.forEach((o) => {
        if(o.includes('americano')) {
            answer += 4500;
        } else if(o.includes('latte')) {
            answer += 5000;
        } else {
            answer += 4500;
        }
    })

    return answer;
}
