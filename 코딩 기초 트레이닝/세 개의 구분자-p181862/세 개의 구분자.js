// https://school.programmers.co.kr/learn/courses/30/lessons/181862

function solution(myStr) {
    const answer = [];
    const op = ['a','b','c'];

    let sub = '';

    myStr = myStr.split("");

    myStr.forEach((s) => {
        if(!op.includes(s)) {
            sub += s;
        } else if(sub.length > 0) {
            answer.push(sub);
            sub = '';
        }
    });

    if(sub.length > 0) answer.push(sub);


    return answer.length === 0 ? ['EMPTY'] : answer;
}
