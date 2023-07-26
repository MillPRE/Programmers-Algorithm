function solution(rny_string) {
    const answer = [];

    rny_string = rny_string.split(""); // 문자 자르기
    rny_string.forEach((d) => {
        if(d === 'm') {
            answer.push('rn');
        } else {
            answer.push(d);
        }
    });

    return answer.join('');
}
