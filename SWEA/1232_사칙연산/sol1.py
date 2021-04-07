import sys
sys.stdin = open('input.txt')


# 후위 탐색
def traversal(n):
    if 1 <= n <= N:
        traversal(left[n])
        traversal(right[n])
        # 후위 연산식 스택에 쌓아주기
        stack.append(values[n])


# 후위 연산
def calculate():
    traversal(1)


    # 숫자를 담아둘 스택
    numbers = []

    while stack:
        elem = stack.pop(0)

        if elem in signs:
            if elem == '+':
                numbers[-1] = numbers[-2] + numbers.pop()
            elif elem == '-':
                numbers[-1] = numbers[-2] - numbers.pop()
            elif elem == '*':
                numbers[-1] = numbers[-2] * numbers.pop()
            elif elem == '/':
                numbers[-1] = numbers[-2] / numbers.pop()
        else:
            numbers.append(elem)
    return int(numbers[0])


for tc in range(1, 11):
    N = int(input())

    signs = ['+', '-', '*', '/']
    left = [0] * (N+1)
    right = [0] * (N+1)
    values = [0] * (N+1)

    # 트리 만들기
    for i in range(N):
        nodes = list(input().split())
        idx = int(nodes[0])
        # 사칙연산을 하는 노드라면
        if nodes[1] in signs:
            values[idx] = nodes[1]
            left[idx] = int(nodes[2])
            right[idx] = int(nodes[3])
        # 단순 숫자 노드라면
        else:
            values[idx] = int(nodes[1])

    # 후위 연산식 스택
    stack = []

    print('#{} {}'.format(tc, calculate()))



