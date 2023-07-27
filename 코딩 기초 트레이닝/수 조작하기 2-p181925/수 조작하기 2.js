// https://school.programmers.co.kr/learn/courses/30/lessons/181925

function solution(numLog) {
    const answer = [];
    let prev = numLog[0];

    for(let i = 1; i < numLog.length ; i++) {
        let next = numLog[i];
        const diff = Math.abs(next - prev);

        if(next > prev) {
            if(diff === 1) {
                answer.push('w');
            } else {
                answer.push('d');
            }
        } else {
            if(diff === 1) answer.push('s');
            else answer.push('a');
        }
        prev = next;
    }

    return answer.join('');
}
