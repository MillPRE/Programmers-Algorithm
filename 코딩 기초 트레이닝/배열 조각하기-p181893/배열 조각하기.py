# https://school.programmers.co.kr/learn/courses/30/lessons/181893

def solution(arr, query):
    for index, q in enumerate(query):
        if index % 2 == 0:
            arr = [x for i, x in enumerate(arr) if i <= q]
        else:
            arr = [x for i, x in enumerate(arr) if i >= q]

    return arr
