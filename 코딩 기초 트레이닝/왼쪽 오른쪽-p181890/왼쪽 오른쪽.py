# https://school.programmers.co.kr/learn/courses/30/lessons/181890

def solution(str_list):
    answer = []

    l = -1
    r = -1

    if 'l' in str_list:
        l = str_list.index('l')

    if 'r' in str_list:
        r = str_list.index('r')


    if l > -1 and r > -1:
        if l < r :
            return str_list[0:l]
        else:
            return str_list[r+1:]
    elif l > -1 and r < 0:
        return str_list[0:l]
    elif r > -1 and l < 0:
        return str_list[r+1:]
    else:
        return []

    return answer
