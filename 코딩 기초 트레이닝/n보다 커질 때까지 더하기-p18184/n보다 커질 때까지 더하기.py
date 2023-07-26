# https://school.programmers.co.kr/learn/courses/30/lessons/181884

def solution(numbers, n):
    answer = 0

    for num in numbers:

        if (answer + num) <= n:
            answer += num
        else:
            answer += num
            break

    return answer
