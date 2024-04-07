def solution(s):
    stack = []
    s = list(s)

    def isEmpty(stack):
        return len(stack) == 0

    for i in s:
        if i == ')':
            if isEmpty(stack):
                return False
            if stack[-1] == '(':
                stack.pop()
        else:
            stack.append(i)

    return True if isEmpty(stack) else False