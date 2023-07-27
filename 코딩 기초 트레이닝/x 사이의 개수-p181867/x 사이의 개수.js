// https://school.programmers.co.kr/learn/courses/30/lessons/181867

function solution(myString) {
    const answer = [];
    let lens = 0;

    myString.split("").forEach((m) => {
        if(m !== 'x') {
            lens++;
        }
        else {
            answer.push(lens);
            lens = 0;
        }
    });

    answer.push(lens);
    return answer;
}
