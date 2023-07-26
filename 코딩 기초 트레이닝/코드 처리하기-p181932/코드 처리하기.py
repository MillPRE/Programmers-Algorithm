def solution(code):
    answer = ''

    code = list(code)
    mode = False
    for index, value in enumerate(code):
        if value == '1':
            mode = not mode
        elif (index % 2 == 0 and (not mode)) or (index % 2 != 0 and mode):
            answer += value

    return answer if len(answer) > 0 else 'EMPTY'
