from collections import deque

def solution(people, limit):
    # 보트 한번에 2명만 가능
    # limit 보트 무게 제한

    people.sort(reverse=True)
    people = deque(people)
    cnt = 0

    while len(people) > 0:
        if len(people) == 1:
            cnt += 1
            people.popleft()
        elif people[0] + people[-1] <= limit:
            people.popleft()
            people.pop()
            cnt += 1
        else:
            cnt +=1
            people.popleft()
    return cnt

peoples = [
    [70, 50, 80, 50],
    [70, 80, 50],
    [20, 20, 20, 20, 20, 80]
]

limits = [100, 100, 100]

results = [3, 3, 2]

for idx in range(len(peoples)):
    print(f'test_case #{idx}: {peoples[idx]}')
    people = peoples[idx]
    limit = limits[idx]
    answer = solution(people, limit)
    print(f'return answer: {answer}, real_answer: {results[idx]}')
    print(f'{"PASS" if answer == results[idx] else "FAIL"}\n')