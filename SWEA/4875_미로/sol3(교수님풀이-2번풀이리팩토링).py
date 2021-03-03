import sys
from pandas import DataFrame
sys.stdin = open('sample_input.txt')

def dfs(x, y):
    global found

    if matrix[y][x] == 3:
        found = 1
    else:
        matrix[y][x] = 1
        dys = [-1, 1, 0 ,0]
        dxs = [0, 0, -1, 1]
        for idx in range(4):
            dy, dx = dys[idx], dxs[idx]
            if 0 <= x + dx < N and 0 <= y + dy < N and matrix[y + dy][x + dx] != 1:
                    dfs(x + dx, y + dy)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]

    for y in range(N):
        for x in range(N):
            if matrix[y][x] == 2:
                start = (x, y)
            elif matrix[y][x] == 3:
                goal = (x, y)

    found = 0

    dfs(*start)

    print('#{} {}'.format(tc, found))