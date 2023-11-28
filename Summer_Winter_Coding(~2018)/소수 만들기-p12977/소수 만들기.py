// https://school.programmers.co.kr/learn/courses/30/lessons/12977

def solution(nums):
    answer = 0
    combinations = []

    for i in range(len(nums) -2):
        for j in range(i+1, len(nums) -1):
            for k in range(j+1, len(nums)):
                combinations.append([nums[i], nums[j], nums[k]])

    for combi in combinations:
        sum = combi[0] + combi[1] + combi[2]
        flag = True;

        for i in range(2, sum):
            if ( sum % i == 0):
                flag = False

        if (flag):
            print(sum)
            answer += 1

    return answer