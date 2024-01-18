def solution(food):
    answer = ''
    # fodd[i] => 음식의 개수

    for idx in range(1, len(food)):
        answer += (food[idx] // 2) * str(idx)
    answer = answer + '0' + answer[::-1]
    return answer