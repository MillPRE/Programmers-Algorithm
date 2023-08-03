// https://school.programmers.co.kr/learn/courses/30/lessons/181829

function solution(board, k) {
    var answer = 0;

    board.forEach((b, i) => {
        b.forEach((v, j) => {
            if(i+j <= k) answer += board[i][j];
        });
    });

    return answer;
}
