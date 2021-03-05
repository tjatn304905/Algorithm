import sys
sys.stdin = open('input.txt')

def solution(matrix, x, y):
    stack = [[x, y]]
    dxs = [0, 0, -1, 1]
    dys = [-1, 1, 0 ,0]

    while stack:
        [x, y] = stack.pop(0)
        for idx in range(4):
            dx, dy = dxs[idx], dys[idx]
            if matrix[y + dy][x + dx] == 0:
                stack.append([x + dx, y + dy])
                matrix[y + dy][x + dx] = 1
            elif matrix[y + dy][x + dx] == 3:
                return 1
    return 0


for _ in range(1, 11):
    tc = int(input())
    matrix = [list(map(int, input())) for _ in range(16)]

    for y in range(16):
        for x in range(16):
            if matrix[y][x] == 2:
                start = (x, y)
            elif matrix[y][x] == 3:
                goal = (x, y)

    print('#{} {}'.format(tc, solution(matrix, *start)))