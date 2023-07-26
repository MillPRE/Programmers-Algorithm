function solution(num_str) {
    let answer = 0;

    num_str = num_str.split("");
    num_str.forEach((n) => {
        answer += Number(n);
    });

    return answer;
}
