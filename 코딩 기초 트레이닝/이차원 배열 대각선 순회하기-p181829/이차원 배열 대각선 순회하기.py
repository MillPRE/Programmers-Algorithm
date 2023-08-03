# https://school.programmers.co.kr/learn/courses/30/lessons/181829

def solution(board, k):
    answer = 0

    for i, b in enumerate(board):
        for j, v in enumerate(b):
            if i+j <= k:
                answer += board[i][j]

    return answer
