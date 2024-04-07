from itertools import permutations

# 1. 조합 만들기
# 2. 중복 조합 삭제
# 3. 소수 판별


def solution(numbers):
    answer = []
    numbers = list(numbers)
    perm = []

    for i in range(1, len(numbers) + 1):
        perm += list(permutations(numbers, i))

    nums = [int(("".join(p))) for p in perm]
    nums = list(set(nums))

    for n in nums:
        flag = True
        if n < 2:
            flag = False

        for i in range(2, n):
            if n % i == 0:
                flag = False
                break
        if flag:
            answer.append(n)

    return len(answer)


