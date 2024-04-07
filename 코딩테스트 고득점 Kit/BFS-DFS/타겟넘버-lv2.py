answer = 0


def solution(numbers, target):
    def dfs(idx, cur):
        if len(numbers) == idx:
            if cur == target:
                global answer
                answer += 1
            return 0

        dfs(idx + 1, cur + numbers[idx])
        dfs(idx + 1, cur - numbers[idx])

    dfs(0, 0)

    global answer
    return answer