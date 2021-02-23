import sys
sys.stdin = open('input.txt')

def solution(length, password):
    stack = []
    for i in range(int(length)):
        if i > 0 and stack and stack[-1] == password[i]:
            stack.pop()
        else:
            stack.append(password[i])
    result = ''
    for num in stack:
        result += num
    return(result)


T = 10

for tc in range(1, T+1):
    length, password = input().split()

    print('#{} {}'.format(tc, solution(length, password)))
