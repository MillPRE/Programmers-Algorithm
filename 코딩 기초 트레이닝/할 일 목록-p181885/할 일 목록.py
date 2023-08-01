# https://school.programmers.co.kr/learn/courses/30/lessons/181885

def solution(todo_list, finished):
    answer = []

    for index, t in enumerate(todo_list):
        if(not finished[index]):
            answer.append(t)

    return answer
