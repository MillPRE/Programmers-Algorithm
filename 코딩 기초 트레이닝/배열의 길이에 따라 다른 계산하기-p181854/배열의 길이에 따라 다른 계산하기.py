def solution(arr, n):
    answer = []

    # flag == 0 짝수, != 0 홀수
    flag = len(arr) % 2


    if flag : #홀수
        for index, d in enumerate(arr):
            answer.append(d + (0 if index % 2 != 0 else n))
    else : # 짝수
        for index, d in enumerate(arr):
            answer.append(d + (0 if index % 2 == 0 else n))

    return answer
