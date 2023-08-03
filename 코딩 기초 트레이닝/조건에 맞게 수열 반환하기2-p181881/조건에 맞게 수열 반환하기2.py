# https://school.programmers.co.kr/learn/courses/30/lessons/181881

def solution(arr):
    # a >= 50 짝수 /2
    # a >= 50 홀수 *2 +1
    answer = 0

    flag = True

    while flag:
        inner_flag = False
        for i, a in enumerate(arr):
            if a >= 50 and a % 2 == 0:
                arr[i] = a/2
                inner_flag = True
            elif a <= 50 and a % 2 != 0:
                arr[i] = a*2 +1
                inner_flag = True

        if inner_flag :
            answer += 1
        else:
            flag = False

    return answer
