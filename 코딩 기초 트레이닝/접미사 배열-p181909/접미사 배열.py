# https://school.programmers.co.kr/learn/courses/30/lessons/181909

def solution(my_string):
    answer = []
    my_string = my_string[::-1]
    for i in range(len(my_string)):
        i = i+1
        answer.append(my_string[:i][::-1])
    answer.sort()

    return answer
