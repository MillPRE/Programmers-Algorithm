function solution(code) {
    let answer = '';
    let mode = false;

    // mode 0
    // 값이 1이 아닐때 idx가 짝수일때만 ret의 맨 뒤에 추가
    // 값이 1 이면 mode를 1로 변환

    // mode 1
    // 값이 1이 아닐때 idx가 홀수일때만 ret의 맨 뒤에 추가
    // 값이 1이면 mode를 1에서 0으로 변경

    code = code.split("");
    code.forEach((c, index) => {
        if(c === '1') {
            mode = !mode;
        } else {
            if(index % 2 === 0 && !mode) {
                // index % 2 === 0 짝수 인덱스 mode가 0일때
                answer += c
            } else if(index % 2 !== 0 && mode) {
                // index % 2 !== 0 홀수 인덱스 mode가 1일때
                answer += c
            }
        }
    });

    return answer.length === 0 ? 'EMPTY' : answer;
}
